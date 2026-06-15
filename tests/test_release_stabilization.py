"""Release stabilization regression tests for commit e6a1cea.

This module contains regression tests that verify fixes for lint defects identified during release stabilization:

- F821 (undefined names): Tests for proper variable references
- F811 (redefinitions): Tests for duplicate dictionary key removal
- F601 (dictionary key repeated): Tests for icon definition fixes

These tests ensure that previously undefined references, incorrect method calls,
and duplicate keys remain fixed in future releases.
"""

from pathlib import Path

from ibmdiagrams.ibmbase.build import Build
from ibmdiagrams.ibmbase.colors import Colors
from ibmdiagrams.ibmbase.common import Common
from ibmdiagrams.ibmbase.icons import Icons
from ibmdiagrams.ibmbase.properties import Properties
from ibmdiagrams.ibmbase.types import Types
from ibmdiagrams.ibmscripts.mcp import generate_diagram, generate_from_python_code


def make_build() -> Build:
    """Create a Build instance with empty diagram data."""
    return Build(Common(), Properties())


def test_invalid_connector_style_returns_none_without_name_error():
    """Invalid connector style validation reports the bad value instead of crashing."""
    build = make_build()
    connector = {
        "conn-1": {
            "linecolor": Colors.lines["black"],
            "linetype": "zigzag",
            "startarrow": "",
            "endarrow": "",
            "fontname": "IBM Plex Sans",
            "fontsize": 14,
        }
    }

    assert build.checkConnectors(connector) is None


def test_fill_color_validation_uses_same_family_or_neutral_fill():
    """Fill colors are accepted only when neutral or from the line-color family."""
    build = make_build()
    network_line = build.checkLineColor("network")

    assert build.checkFillColor(network_line, "network") == Colors.fills["network"]
    assert build.checkFillColor(network_line, "white") == Colors.fills["white"]
    assert build.checkFillColor("", "white") == Colors.fills["white"]
    assert build.checkFillColor("", "network") is None
    assert build.checkFillColor(network_line, "compute") is None
    assert build.checkFillColor(network_line, "not-a-color") is None


def test_shape_builder_returns_drawio_cell_without_undefined_header():
    """The dynamic shape builder returns a DrawIO cell payload without legacy header data."""
    types = Types(Common())
    node = {
        "shape": "pnode",
        "label": "Virtual Server",
        "sublabel": "10.0.0.4",
        "genname": "Virtual Server",
        "linecolor": Colors.lines["compute"],
        "fillcolor": Colors.fills["compute"],
        "parentid": None,
        "image": "",
        "icon": "ibm-cloud--virtual-server-vpc",
    }

    shape = types.buildShape("shape-1", node, 10, 20, 48, 48, {"owner": "test"}, False)

    assert "header" not in shape
    assert shape["cell"]["id"] == "shape-1"
    assert shape["cell"]["parent"] == "1"
    assert "Virtual Server" in shape["cell"]["value"]
    assert shape["props"] == {"owner": "test"}


def test_value_builder_uses_text_style_without_undefined_shape_map():
    """Value builder uses the built-in text style instead of an undefined shape map."""
    types = Types(Common())

    value = types.buildValue("value-1", "parent-1", "", "", "", "hello", 1, 2, 3, 4)

    assert value["cell"]["id"] == "value-1"
    assert value["cell"]["parent"] == "parent-1"
    assert value["cell"]["value"] == "hello"
    assert value["cell"]["style"].startswith("text;html=1;")


def test_enterprise_icon_fill_keeps_existing_effective_value():
    """Removing the duplicate dictionary key preserves the previously effective fill value."""
    icon = Icons(Common()).getIconDictionary()["Enterprise Icon"]

    assert icon["color"] == Colors.lines["user"]
    assert icon["fill"] == Colors.lines["compute"]


def test_mcp_generate_from_python_code_helper_writes_drawio(tmp_path: Path):
    """MCP code helper executes diagram-as-code and writes the requested DrawIO file."""
    output = str(tmp_path)
    python_code = f"""
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, VPC

with Diagram("mcp-code-smoke", output={output!r}):
    with IBMCloud("IBM Cloud"):
        with VPC("Smoke VPC"):
            VirtualServer("Smoke VSI")
"""

    result = generate_from_python_code(python_code, outputfolder=output)

    assert result["status"] == "success"
    assert Path(result["outputfile"]).exists()
    assert result["outputfile"].endswith("mcp-code-smoke.drawio")


def test_mcp_generate_diagram_helper_writes_drawio_from_json(tmp_path: Path):
    """MCP file helper generates DrawIO output from the bundled JSON example."""
    inputfile = Path("docs/examples/json/cloud.json")

    result = generate_diagram(str(inputfile), outputfolder=str(tmp_path))

    assert result["codetype"] == "DRAWIO"
    assert result["labeltype"] == "CUSTOM"
    assert Path(result["outputfile"]).exists()
    assert result["outputfile"].endswith("cloud.drawio")
