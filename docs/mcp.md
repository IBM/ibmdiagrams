# Model Context Protocol (MCP) Integration

IBM Diagrams provides a Model Context Protocol (MCP) server that enables AI assistants and other MCP clients to generate architecture diagrams programmatically.

> **🚀 New to MCP?** Check out our [**Onboarding and Setup Guide**](mcp-onboarding.md) for step-by-step instructions to configure IBM Bob or Claude Desktop.

---

## 📋 Table of Contents

1. [What is MCP?](#what-is-mcp)
2. [Quick Start](#quick-start)
3. [Configuration](#configuration)
4. [Available Tools](#available-tools)
5. [Usage Examples](#usage-examples)
6. [Troubleshooting](#troubleshooting)

---

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open protocol that standardizes how applications provide context to Large Language Models (LLMs). IBM Diagrams implements an MCP server using [FastMCP](https://github.com/jlowin/fastmcp), allowing AI assistants to:

- Generate diagrams from Terraform state files
- Generate diagrams from JSON input files
- Convert infrastructure to Python diagram code
- Customize diagram output (labels, fonts, output format)

---

## Quick Start

### Prerequisites

- Python 3.11+
- IBM Diagrams installed (see [Setup Guide](setup.md))
- An MCP-compatible client (e.g., IBM Bob, Claude Code etc.)

### Test the MCP Server

```bash
# Test the server directly
ibmdiagrams --mcp

# Or with uv
uv run ibmdiagrams --mcp

# Or using uvx with a wheel file
uvx /path/to/ibmdiagrams-3.3.0-py3-none-any.whl --mcp
```

The server will start and display available tools and connection information.

---

## Configuration

### Method 1: Using Installed CLI

If you have `ibmdiagrams` installed globally or in your PATH:

```json
{
  "mcpServers": {
    "ibmdiagrams-cli": {
      "command": "ibmdiagrams",
      "args": ["--mcp"]
    }
  }
}
```

### Method 2: Using uvx with Wheel File

For development or when using a specific wheel file:

```json
{
  "mcpServers": {
    "ibmdiagrams": {
      "command": "uvx",
      "args": [
        "/Users/username/path/to/ibmdiagrams-3.3.0-py3-none-any.whl",
        "--mcp"
      ]
    }
  }
}
```

### Method 3: Using uv run (Development)

For development with the source repository:

```json
{
  "mcpServers": {
    "ibmdiagrams-dev": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/username/path/to/ibmdiagrams",
        "ibmdiagrams",
        "--mcp"
      ]
    }
  }
}
```

### Configuration File Locations

**IBM Bob:**
- `.bob/mcp.json` in your workspace root

---

## Available Tools

The IBM Diagrams MCP server provides three tools:

### 1. `generate_from_file`

Generate an architecture diagram from a Terraform state file or JSON input file.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `inputfile` | string | ✅ Yes | - | Path to input file (`.tfstate` or `.json`) |
| `outputfolder` | string | ❌ No | `""` | Output directory path (empty = current directory) |
| `labeltype` | string | ❌ No | `"CUSTOM"` | Label type: `"CUSTOM"` or `"GENERAL"` |
| `codetype` | string | ❌ No | `"DRAWIO"` | Output format: `"DRAWIO"` or `"PYTHON"` |
| `fontname` | string | ❌ No | `"IBM Plex Sans"` | Font family name |

**Label Types:**
- **CUSTOM**: Shows resource names, IP addresses, and specific details
- **GENERAL**: Shows only resource types (e.g., "Virtual Server", "VPC")

**Code Types:**
- **DRAWIO**: Generates `.drawio` file for draw.io desktop
- **PYTHON**: Generates `.py` file with diagram-as-code

**Supported Fonts:**
- `"IBM Plex Sans"` (default)
- `"IBM Plex Sans Arabic"`
- `"IBM Plex Sans Devanagari"`
- `"IBM Plex Sans Hebrew"`
- `"IBM Plex Sans JP"`
- `"IBM Plex Sans KR"`
- `"IBM Plex Sans Thai"`

**Returns:**

```json
{
  "inputfile": "cloud.tfstate",
  "outputfile": "cloud.drawio",
  "provider": "IBMCLOUD",
  "labeltype": "CUSTOM",
  "codetype": "DRAWIO",
  "fontname": "IBM Plex Sans"
}
```

### 2. `generate_from_code`

Generate a DrawIO diagram by executing Python diagram-as-code directly from a string.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `python_code` | string | ✅ Yes | - | Python code using ibmdiagrams API |
| `diagram_name` | string | ❌ No | `"diagram"` | Name for output diagram file (without extension) |
| `outputfolder` | string | ❌ No | `""` | Output directory path (empty = current directory) |
| `fontname` | string | ❌ No | `"IBM Plex Sans"` | Font family name |

**Python Code Requirements:**
- Must use the ibmdiagrams API with context manager pattern
- Must include `with Diagram(...)` to define diagram structure
- All necessary imports must be included in the code string

**Example Python Code:**
```python
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, VPC
from ibmdiagrams.ibmcloud.compute import VirtualServer

with Diagram("my-architecture"):
    with IBMCloud("IBM Cloud"):
        with VPC("Production VPC"):
            vsi = VirtualServer("Web Server")
```

**Supported Fonts:**
- `"IBM Plex Sans"` (default)
- `"IBM Plex Sans Arabic"`
- `"IBM Plex Sans Devanagari"`
- `"IBM Plex Sans Hebrew"`
- `"IBM Plex Sans JP"`
- `"IBM Plex Sans KR"`
- `"IBM Plex Sans Thai"`

**Returns:**

```json
{
  "diagram_name": "my-architecture",
  "outputfile": "./my-architecture.drawio",
  "fontname": "IBM Plex Sans",
  "status": "success"
}
```

### 3. `server_info`

Get metadata about the IBM Diagrams MCP server.

**Parameters:** None

**Returns:**

```json
{
  "name": "IBM Diagrams",
  "tools": ["generate_from_file", "generate_from_code", "server_info"],
  "supported_input_types": ["json", "tfstate", "python_code"],
  "supported_code_types": ["DRAWIO", "PYTHON"],
  "supported_label_types": ["CUSTOM", "GENERAL"]
}
```

---

## Usage Examples

### Example 1: Generate DrawIO Diagram with Custom Labels

**Request:**
```json
{
  "tool": "generate_from_file",
  "arguments": {
    "inputfile": "/path/to/infrastructure.tfstate"
  }
}
```

**Result:**
- Creates `infrastructure.drawio` in the same directory
- Uses custom labels (resource names, IPs)
- Uses IBM Plex Sans font

### Example 2: Generate Python Code with General Labels

**Request:**
```json
{
  "tool": "generate_from_file",
  "arguments": {
    "inputfile": "/path/to/infrastructure.tfstate",
    "labeltype": "GENERAL",
    "codetype": "PYTHON"
  }
}
```

**Result:**
- Creates `infrastructure.py` with diagram-as-code
- Uses general labels (resource types only)
- Can be edited and re-run to regenerate diagram

### Example 3: Custom Output Location and Font

**Request:**
```json
{
  "tool": "generate_from_file",
  "arguments": {
    "inputfile": "/path/to/infrastructure.tfstate",
    "outputfolder": "/path/to/diagrams",
    "fontname": "IBM Plex Sans JP"
  }
}
```

**Result:**
- Creates `/path/to/diagrams/infrastructure.drawio`
- Uses Japanese font variant
- Uses custom labels

### Example 4: JSON Input File

**Request:**
```json
{
  "tool": "generate_from_file",
  "arguments": {
    "inputfile": "/path/to/architecture.json"
  }
}
```

**Result:**
- Creates `architecture.drawio` from JSON input
- JSON format is internal and not externally documented

### Example 5: Generate from Python Code String

**Request:**
```json
{
  "tool": "generate_from_code",
  "arguments": {
    "python_code": "from ibmdiagrams.ibmcloud.diagram import Diagram\nfrom ibmdiagrams.ibmcloud.groups import IBMCloud, VPC\nfrom ibmdiagrams.ibmcloud.compute import VirtualServer\n\nwith Diagram('my-architecture'):\n    with IBMCloud('IBM Cloud'):\n        with VPC('Production VPC'):\n            vsi = VirtualServer('Web Server')",
    "diagram_name": "my-architecture",
    "outputfolder": "/path/to/output"
  }
}
```

**Result:**
- Creates `/path/to/output/my-architecture.drawio`
- Executes the Python code to generate the diagram
- No intermediate files created

### Example 6: Generate from Python Code with Custom Font

**Request:**
```json
{
  "tool": "generate_from_code",
  "arguments": {
    "python_code": "from ibmdiagrams.ibmcloud.diagram import Diagram\nfrom ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC\nfrom ibmdiagrams.ibmcloud.compute import VirtualServer\n\nwith Diagram('tokyo-architecture'):\n    with IBMCloud('IBM Cloud'):\n        with Region('Tokyo'):\n            with VPC('Production VPC'):\n                vsi = VirtualServer('Web Server')",
    "diagram_name": "tokyo-architecture",
    "fontname": "IBM Plex Sans JP"
  }
}
```

**Result:**
- Creates `tokyo-architecture.drawio` in current directory
- Uses Japanese font variant for proper rendering
- Ideal for localized documentation

### Example 7: Get Server Information

**Request:**
```json
{
  "tool": "server_info",
  "arguments": {}
}
```

**Result:**
```json
{
  "name": "IBM Diagrams",
  "tools": ["generate_from_file", "generate_from_code", "server_info"],
  "supported_input_types": ["json", "tfstate", "python_code"],
  "supported_code_types": ["DRAWIO", "PYTHON"],
  "supported_label_types": ["CUSTOM", "GENERAL"]
}
```

---

## AI Assistant Usage

When using IBM Diagrams with an AI assistant (like IBM Bob, or Claude), you can ask natural language questions. The assistant will use the MCP server to execute these requests and provide feedback on the results.

### Example Prompts

#### Basic Diagram Generation

**Generate from Terraform state:**
```
Use the ibmdiagrams MCP server to create a diagram from 'docs/examples/terraform/cloud.tfstate'.
Save the diagram in the current folder.
```

**Generate from JSON input:**
```
Use the ibmdiagrams MCP server to generate a diagram from 'docs/examples/json/cloud.json'.
```

**Simple request:**
```
Generate a diagram from my Terraform state file at ./infrastructure.tfstate
```

#### Custom Label Types

**Use general labels (resource types only):**
```
Create a diagram from ./infrastructure.tfstate with general labels. This should show
resource types like "Virtual Server" and "VPC" instead of specific names.
```

**Use custom labels (default - shows names and IPs):**
```
Generate a diagram from ./infrastructure.tfstate with custom labels showing all
resource names and IP addresses.
```

#### Output Format Options

**Generate Python code instead of DrawIO:**
```
Convert my Terraform state file ./infrastructure.tfstate to Python diagram code
so I can customize it later. Use the PYTHON output format.
```

**Generate DrawIO file (default):**
```
Create a DrawIO diagram from ./infrastructure.tfstate that I can open in draw.io desktop.
```

#### Custom Output Location

**Specify output folder:**
```
Create a diagram from ./infrastructure.tfstate with general labels and
output it to the ./docs folder.
```

**Save to specific directory:**
```
Generate a diagram from ./docs/examples/terraform/cloud.tfstate and save it to ./diagrams/architecture/
```

#### Font Customization

**Use Japanese fonts:**
```
Generate a diagram from ./infrastructure.tfstate using IBM Plex Sans JP font
for Japanese text support.
```

**Use Arabic fonts:**
```
Create a diagram from ./infrastructure.tfstate with IBM Plex Sans Arabic font.
```

**Other supported fonts:**
```
Generate a diagram using IBM Plex Sans KR font (Korean)
Generate a diagram using IBM Plex Sans Hebrew font
Generate a diagram using IBM Plex Sans Thai font
Generate a diagram using IBM Plex Sans Devanagari font
```

#### Natural Language to Diagram (Using generate_from_code)

**Create diagram from description:**
```
Create a diagram showing a 3-zone VPC with a load balancer and two web servers.
Use the generate_from_code tool to build this from scratch.
```

**Build custom architecture:**
```
I need a diagram with:
- IBM Cloud container
- Dallas region
- Production VPC with CIDR 10.10.0.0/16
- Two zones (Zone 1 and Zone 2)
- Each zone has a subnet with a virtual server
- Connect them with a load balancer

Generate the Python code and create the diagram using generate_from_code.
```

**Quick prototype:**
```
Generate a simple diagram showing IBM Cloud with a VPC containing a single virtual server.
Use generate_from_code to create it directly.
```

#### Combined Options

**Full customization:**
```
Use the ibmdiagrams MCP server to:
1. Read the Terraform state file at ./infrastructure.tfstate
2. Generate a diagram with general labels
3. Use IBM Plex Sans JP font
4. Output to ./docs/diagrams/ folder
5. Generate as Python code (not DrawIO)
```

**Production diagram with specific settings:**
```
Create a production-ready diagram from ./prod-infrastructure.tfstate with:
- Custom labels showing all resource details
- Output to ./documentation/architecture/
- DrawIO format for editing
```

#### Workflow Examples

**Review and iterate:**
```
1. Generate a diagram from ./infrastructure.tfstate
2. Review the output
3. If needed, regenerate with general labels for a cleaner view
```

**Documentation workflow:**
```
1. Generate Python code from ./infrastructure.tfstate
2. Review and customize the Python code
3. Run the Python code to generate the final DrawIO diagram
```

**Multi-environment setup:**
```
Generate diagrams for all environments:
- ./terraform/dev.tfstate → ./docs/dev-architecture.drawio
- ./terraform/staging.tfstate → ./docs/staging-architecture.drawio
- ./terraform/prod.tfstate → ./docs/prod-architecture.drawio
```

### Tips for Effective Prompts

1. **Be specific about file paths**: Use relative or absolute paths
2. **Mention output preferences**: Specify DrawIO vs Python, custom vs general labels
3. **Include context**: Describe what the infrastructure contains if relevant
4. **Request specific features**: Font types, output folders, label styles
5. **Chain requests**: Ask for generation, review, and regeneration if needed

---

## Troubleshooting

### Server Won't Start

**Symptoms:**
```
Error: Failed to start MCP server
```

**Solutions:**

1. **Verify installation:**
   ```bash
   ibmdiagrams --version
   ```

2. **Test server manually:**
   ```bash
   ibmdiagrams --mcp
   ```

3. **Check Python version:**
   ```bash
   python --version  # Should be 3.11+
   ```

4. **Reinstall package:**
   ```bash
   pip install --force-reinstall ibmdiagrams-*.whl
   ```

### Tool Not Found

**Symptoms:**
```
Error: Tool 'generate_from_file' not found
```

**Solutions:**

1. **Verify server is running:**
   - Check MCP client logs
   - Restart the MCP client

2. **Check configuration:**
   - Verify `command` path is correct
   - Verify `args` includes `["--mcp"]`

3. **Test server info:**
   ```
   Use the server_info tool to verify available tools
   ```

### File Not Found Errors

**Symptoms:**
```
Error: Input file not found: /path/to/file.tfstate
```

**Solutions:**

1. **Use absolute paths:**
   ```json
   {
     "inputfile": "/Users/username/project/infrastructure.tfstate"
   }
   ```

2. **Verify file exists:**
   ```bash
   ls -la /path/to/file.tfstate
   ```

3. **Check file permissions:**
   ```bash
   chmod 644 /path/to/file.tfstate
   ```

### Font Not Rendering

**Symptoms:**
- Diagram generated but fonts don't render correctly in draw.io

**Solutions:**

1. **Install IBM Plex Sans fonts** (see [Setup Guide](setup.md#font-installation))

2. **Restart draw.io desktop** after installing fonts

3. **Use alternative font temporarily:**
   ```json
   {
     "inputfile": "infrastructure.tfstate",
     "fontname": "Arial"
   }
   ```

### Permission Errors

**Symptoms:**
```
Error: Permission denied writing to output folder
```

**Solutions:**

1. **Check output folder permissions:**
   ```bash
   ls -la /path/to/output
   ```

2. **Use current directory:**
   ```json
   {
     "inputfile": "infrastructure.tfstate",
     "outputfolder": ""
   }
   ```

3. **Create output directory:**
   ```bash
   mkdir -p /path/to/output
   chmod 755 /path/to/output
   ```

---

## Advanced Configuration

### Multiple Server Instances

You can configure multiple MCP server instances for different purposes:

```json
{
  "mcpServers": {
    "ibmdiagrams-prod": {
      "command": "ibmdiagrams",
      "args": ["--mcp"]
    },
    "ibmdiagrams-dev": {
      "command": "uvx",
      "args": [
        "/path/to/dev/ibmdiagrams-3.3.0-py3-none-any.whl",
        "--mcp"
      ]
    }
  }
}
```

### Working Directory

Specify a working directory for the server:

```json
{
  "mcpServers": {
    "ibmdiagrams": {
      "command": "ibmdiagrams",
      "args": ["--mcp"],
      "cwd": "/path/to/project"
    }
  }
}
```

---

## Integration Examples

### IBM Bob

1. Create `.bob/mcp.json` in your workspace:
   ```json
   {
     "mcpServers": {
       "ibmdiagrams": {
         "command": "ibmdiagrams",
         "args": ["--mcp"]
       }
     }
   }
   ```

2. Restart the MCP Server

3. Ask IBM Bob to generate diagrams:
   ```
   Use the ibmdiagrams MCP server to create a diagram from infrastructure.tfstate
   ```

---

## API Reference

### FastMCP Implementation

IBM Diagrams uses [FastMCP](https://github.com/jlowin/fastmcp) for the MCP server implementation. The server is defined in [`src/ibmdiagrams/ibmscripts/mcp.py`](../src/ibmdiagrams/ibmscripts/mcp.py).

**Key Components:**

- **Server Name**: `"IBM Diagrams"`
- **Version**: Dynamically retrieved from package metadata
- **Protocol**: Model Context Protocol (MCP)
- **Transport**: Standard input/output (stdio)

**Tool Registration:**

```python
@mcp.tool
def generate_from_file(
    inputfile: str,
    outputfolder: str = "",
    labeltype: str = "CUSTOM",
    codetype: str = "DRAWIO",
    fontname: str = "IBM Plex Sans",
) -> dict[str, str]:
    """Generate an ibmdiagrams output file from a .json or .tfstate input file."""
    # Implementation
```

---

## AI Skill for Enhanced Integration

For AI assistants like IBM Bob, Claude Code, Cursor, and others, we provide a **portable AI skill** that makes working with IBM Diagrams even easier.

### What is the AI Skill?

The **ibmdiagrams-builder skill** turns any AI agent into an expert IBM architecture diagram engineer. It provides:

- 🎯 **Automatic activation** when you ask about architecture diagrams or Terraform visualization
- 📚 **Comprehensive knowledge** of all IBM Cloud components and best practices
- 🔧 **MCP integration** that uses the ibmdiagrams MCP server tools correctly
- 📖 **Guided workflows** for common diagram generation tasks
- ✅ **Quality checks** to ensure IBM Design Language compliance

### Installation

**For IBM Bob:**
```bash
# Project-scoped (recommended for teams)
mkdir -p .bob/skills
cp -r skills/ibmdiagrams-builder .bob/skills/

# Or global (available in all projects)
mkdir -p ~/.bob/skills
cp -r skills/ibmdiagrams-builder ~/.bob/skills/
```

**For Claude Code:**
```bash
# Project-scoped
mkdir -p .claude/skills
cp -r skills/ibmdiagrams-builder .claude/skills/

# Or global
mkdir -p ~/.claude/skills
cp -r skills/ibmdiagrams-builder ~/.claude/skills/
```

**For other AI assistants** (Cursor, Windsurf, Copilot, Cline, Continue.dev, Aider), see the [skill README](../skills/ibmdiagrams-builder/README.md) for specific installation instructions.

### Usage

Once installed, the skill activates automatically when you ask about:

- Creating architecture diagrams from Terraform state files
- Generating diagrams using Python diagram-as-code
- IBM Cloud infrastructure visualization
- DrawIO diagram generation
- IBM Design Language technical diagrams

**Example prompts:**
```
Generate a diagram from my Terraform state file at ./infrastructure.tfstate

Create a clean architecture diagram without IP addresses for a presentation

Help me create a diagram for a 3-zone VPC with web and database tiers

Show me how to add a load balancer to my existing diagram code
```

### Benefits

- ✅ **No manual MCP tool calls** — the skill handles tool usage automatically
- ✅ **Best practices built-in** — follows IBM Design Language guidelines
- ✅ **Error recovery** — handles common issues and provides helpful guidance
- ✅ **Multi-client support** — works with 8+ different AI assistants
- ✅ **Always up-to-date** — skill updates independently of the MCP server

For complete documentation, see the [AI Skill README](../skills/ibmdiagrams-builder/README.md).

---

## Related Documentation

- **[Setup Guide](setup.md)** - Installation and configuration
- **[Terraform Guide](terraform.md)** - Terraform state file integration
- **[Diagram as Code](diagram-as-code.md)** - Python API reference
- **[AI Skill](../skills/ibmdiagrams-builder/README.md)** - Portable AI skill for enhanced integration
- **[Testing Guide](testing.md)** - Testing and validation

---

## External Resources

- **[Model Context Protocol](https://modelcontextprotocol.io/)** - Official MCP documentation
- **[FastMCP](https://github.com/jlowin/fastmcp)** - FastMCP framework
- **[IBM Bob](https://internal.bob.ibm.com/docs/ide/configuration/mcp/mcp-in-bob)** - IBM Bob - Using MCP

---

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).