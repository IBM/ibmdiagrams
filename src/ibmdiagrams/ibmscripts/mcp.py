# @file mcp.py
#
# Copyright contributors to the ibmdiagrams project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from importlib.metadata import version
from os import path
from tempfile import NamedTemporaryFile

from fastmcp import FastMCP

from ibmdiagrams import Common, Compose, Load, _data, _savediagrams
from ibmdiagrams.ibmbase.build import Build
from ibmdiagrams.ibmutils import log_server_banner

logger = logging.getLogger(__name__)

SERVER_NAME = "IBM Diagrams"


def _build_common(
    inputfile: str,
    outputfolder: str = "",
    labeltype: str = "CUSTOM",
    codetype: str = "DRAWIO",
    fontname: str = "IBM Plex Sans",
) -> Common:
    common = Common()
    common.setInputFile(inputfile)
    common.setOutputFolder(outputfolder)
    common.setFontName(fontname)

    if labeltype.upper() == "GENERAL":
        common.setGeneralLabels()
    else:
        common.setCustomLabels()

    if codetype.upper() == "PYTHON":
        common.setPythonCode()
    else:
        common.setDrawioCode()

    return common


def _prepare_input(common: Common, inputfile: str) -> tuple[str, str]:
    basename = path.basename(inputfile)
    inputbase = path.splitext(basename)[0]
    inputtype = path.splitext(basename)[1][1:]

    if inputtype == "json":
        common.setInputJSON()
    elif inputtype == "tfstate":
        common.setInputTerraform()
    else:
        raise ValueError(f"Unsupported input file type: {inputtype}")

    if not path.isfile(common.getInputFile()):
        raise FileNotFoundError(f"Input file not found: {inputfile}")

    output_extension = "py" if common.isPythonCode() else "drawio"
    outputfile = inputbase + "." + output_extension
    common.setOutputFile(outputfile)

    return inputbase, outputfile


def generate_diagram(
    inputfile: str,
    outputfolder: str = "",
    labeltype: str = "CUSTOM",
    codetype: str = "DRAWIO",
    fontname: str = "IBM Plex Sans",
) -> dict[str, str]:
    common = _build_common(
        inputfile=inputfile,
        outputfolder=outputfolder,
        labeltype=labeltype,
        codetype=codetype,
        fontname=fontname,
    )
    _, outputfile = _prepare_input(common, inputfile)

    data = Load(common)
    if not data.loadData():
        raise RuntimeError("Failed to load input data")

    compose = Compose(common, data)
    compose.composeDiagrams()

    provider = common.getProvider()

    # Verify the output file was created
    output_path = path.join(outputfolder, outputfile)
    if not path.exists(output_path):
        raise RuntimeError(f"Failed to generate output file: {output_path}")

    return {
        "inputfile": inputfile,
        "outputfile": output_path,
        "provider": provider.value.upper() if provider else "UNKNOWN",
        "labeltype": labeltype.upper(),
        "codetype": codetype.upper(),
        "fontname": common.getFontName(),
    }


def generate_from_python_code(
    python_code: str,
    diagram_name: str = "diagram",
    outputfolder: str = "",
    fontname: str = "IBM Plex Sans",
) -> dict[str, str]:
    """
    Execute Python diagram-as-code and generate DrawIO output.

    Args:
        python_code: Python code string using ibmdiagrams API
        diagram_name: Name for the output diagram file (without extension)
        outputfolder: Output directory path (default: current directory)
        fontname: Font family name (default: IBM Plex Sans)

    Returns:
        dict with execution results including output file path
    """
    # Clear any previous diagram data
    _data.reset()
    _savediagrams.clear()

    # Create a temporary file to execute the Python code
    with NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as tmp:
        tmp.write(python_code)
        tmp_path = tmp.name

    try:
        # Prepare the execution environment
        exec_globals = {
            "__name__": "__main__",
            "__file__": tmp_path,
        }

        # Execute the Python code
        # Note: exec is used here intentionally to execute user-provided diagram code
        # This is safe in the MCP context as it runs in the user's local environment
        exec(python_code, exec_globals)  # noqa: S102

        # Check if any diagrams were generated
        if not _savediagrams:
            raise RuntimeError(
                "No diagrams were generated. Ensure the code uses 'with Diagram(...)' context."
            )

        # Get the first diagram (or the one matching diagram_name if specified)
        if diagram_name in _savediagrams:
            xmldata = _savediagrams[diagram_name]
            output_name = diagram_name
        else:
            # Use the first available diagram
            output_name = list(_savediagrams.keys())[0]
            xmldata = _savediagrams[output_name]

        # Build and save the diagram
        common = Common()
        common.setInputPython()
        common.setOutputFolder(outputfolder)
        common.setFontName(fontname)

        build = Build(common, _data)
        outputfile = output_name + ".drawio"

        # Write the XML to file
        xml_string = build.getXMLString(xmldata, output_name)
        output_path = path.join(outputfolder, outputfile)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(xml_string)

        # Verify the output file was created
        if not path.exists(output_path):
            raise RuntimeError(f"Failed to generate output file: {output_path}")

        return {
            "diagram_name": output_name,
            "outputfile": output_path,
            "fontname": fontname,
            "status": "success",
        }

    except Exception as e:
        raise RuntimeError(f"Failed to execute Python code: {str(e)}") from e

    finally:
        # Clean up temporary file
        try:
            import os

            os.unlink(tmp_path)
        except Exception as e:
            logger.debug("Failed to cleanup temporary file %s: %s", tmp_path, str(e))


def create_server() -> FastMCP:
    # Get version dynamically from package metadata
    pkg_version = version("ibmdiagrams")

    mcp = FastMCP(
        name=SERVER_NAME,
        version=pkg_version,
    )

    @mcp.tool
    def generate_from_file(
        inputfile: str,
        outputfolder: str = "",
        labeltype: str = "CUSTOM",
        codetype: str = "DRAWIO",
        fontname: str = "IBM Plex Sans",
    ) -> dict[str, str]:
        """Generate an ibmdiagrams output file from a .json or .tfstate input file."""
        return generate_diagram(
            inputfile=inputfile,
            outputfolder=outputfolder,
            labeltype=labeltype,
            codetype=codetype,
            fontname=fontname,
        )

    @mcp.tool
    def generate_from_code(
        python_code: str,
        diagram_name: str = "diagram",
        outputfolder: str = "",
        fontname: str = "IBM Plex Sans",
    ) -> dict[str, str]:
        """Generate a DrawIO diagram by executing Python diagram-as-code.

        This tool accepts Python code that uses the ibmdiagrams API and executes it
        to generate a DrawIO diagram file. The code should use the context manager
        pattern with 'with Diagram(...)' to define the diagram structure.

        Example Python code:
        ```python
        from ibmdiagrams.ibmcloud.diagram import Diagram
        from ibmdiagrams.ibmcloud.groups import IBMCloud, VPC
        from ibmdiagrams.ibmcloud.compute import VirtualServer

        with Diagram("my-architecture"):
            with IBMCloud("IBM Cloud"):
                with VPC("Production VPC"):
                    vsi = VirtualServer("Web Server")
        ```

        Args:
            python_code: Python code string using ibmdiagrams API
            diagram_name: Name for the output diagram file (default: "diagram")
            outputfolder: Output directory path (default: current directory)
            fontname: Font family name (default: "IBM Plex Sans")

        Returns:
            Dictionary with execution results including output file path
        """
        return generate_from_python_code(
            python_code=python_code,
            diagram_name=diagram_name,
            outputfolder=outputfolder,
            fontname=fontname,
        )

    @mcp.tool
    def server_info() -> dict[str, object]:
        """Return basic metadata about the ibmdiagrams MCP server."""
        return {
            "name": SERVER_NAME,
            "tools": ["generate_from_file", "generate_from_code", "server_info"],
            "supported_input_types": ["json", "tfstate", "python_code"],
            "supported_code_types": ["DRAWIO", "PYTHON"],
            "supported_label_types": ["CUSTOM", "GENERAL"],
        }

    return mcp


def main() -> None:
    server = create_server()
    log_server_banner(server)
    server.run(show_banner=False)
