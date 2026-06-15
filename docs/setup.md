# Setup Guide

Complete installation and configuration guide for IBM Diagrams.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Methods](#installation-methods)
3. [Font Installation](#font-installation)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

| Software | Minimum Version | Purpose | Download Link |
|----------|----------------|---------|---------------|
| **Python** | 3.11+ | Runtime environment | [python.org](https://www.python.org/downloads/) |
| **draw.io Desktop** | Latest | View/edit diagrams | [GitHub Releases](https://github.com/jgraph/drawio-desktop/releases) |

### Recommended Software

| Software | Purpose | Download Link |
|----------|---------|---------------|
| **uv** | Fast package manager (10-100x faster than pip) | [astral.sh/uv](https://github.com/astral-sh/uv) |
| **IBM Plex Sans** | Proper font rendering | [Google Fonts](https://fonts.google.com/?query=Plex) |

---

## Installation Methods

### Method 1: Using uv (Recommended) ⚡

**Why uv?**
- 10-100x faster than pip
- Automatic virtual environment management
- Automatic Python version management
- Better dependency resolution

#### Install uv

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (using pip):**
```bash
pip install uv
```

#### Install IBM Diagrams with uv

```bash
# Clone or download the repository
git clone git@github.com:IBM/ibmdiagrams.git
cd ibmdiagrams

# Install all dependencies (creates virtual environment automatically)
uv sync

# Verify installation
uv run ibmdiagrams --help
```

#### Running with uv

```bash
# Run CLI commands
uv run ibmdiagrams cloud.tfstate

# Run Python scripts
uv run python docs/examples/slzvsi.py

# Install additional packages
uv pip install <package-name>
```

---

### Method 2: Using pip (Traditional)

#### Step 1: Install Python

**macOS:**
```bash
# Download from python.org or use Homebrew
brew install python@3.11

# Verify installation
python3 --version
```

**Windows:**
1. Download installer from [python.org](https://www.python.org/downloads/)
2. Run installer and check "Add Python to PATH"
3. Verify: `python --version`

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

#### Step 2: Install pip

```bash
# Usually included with Python 3.11+
# If needed, install manually:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

#### Step 3: Install IBM Diagrams

```bash
# Download wheel from Releases
# https://github.com/your-repo/ibmdiagrams/releases

# Install the package
pip install ibmdiagrams-3.1.10-py3-none-any.whl

# Verify installation
ibmdiagrams --help
```

**Installation Location:**
- **macOS/Linux**: `/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/ibmdiagrams`
- **Windows**: `C:\Users\<username>\AppData\Local\Programs\Python\Python311\Lib\site-packages\ibmdiagrams`

---

### Method 3: Development Installation

For contributors and developers:

```bash
# Clone repository
git clone git@github.com:IBM/ibmdiagrams.git
cd ibmdiagrams

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install in editable mode with dev dependencies
pip install -e .
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest
```

---

## Font Installation

IBM Plex Sans fonts are **required** for proper diagram rendering in draw.io desktop.

### Available Fonts

IBM Diagrams supports these IBM Plex Sans variants:

1. **IBM Plex Sans** (default) - Latin script
2. **IBM Plex Sans Arabic** - Arabic script
3. **IBM Plex Sans Devanagari** - Devanagari script
4. **IBM Plex Sans Hebrew** - Hebrew script
5. **IBM Plex Sans JP** - Japanese script
6. **IBM Plex Sans KR** - Korean script
7. **IBM Plex Sans Thai** - Thai script

### Installation Steps

#### macOS

1. Visit [Google Fonts - IBM Plex](https://fonts.google.com/?query=Plex)
2. Select **IBM Plex Sans** (or desired variant)
3. Click **Get font** → **Download all**
4. Unpack `IBM_Plex_Sans.zip`
5. Open **Font Book** app
6. Select **File** → **Add Fonts to Current User**
7. Select the unpacked folder
8. Restart draw.io desktop

**Verification:**
- Open draw.io desktop
- Create a text box
- Set font to "IBM Plex Sans"
- Type a lowercase "l" - it should have a slight right bend at the bottom

#### Windows

1. Download fonts from [Google Fonts](https://fonts.google.com/?query=Plex)
2. Unpack the ZIP file
3. Select all `.ttf` files
4. Right-click → **Install** (or **Install for all users**)
5. Restart draw.io desktop

#### Linux

```bash
# Download fonts
wget https://fonts.google.com/download?family=IBM%20Plex%20Sans -O ibm-plex-sans.zip

# Create fonts directory if it doesn't exist
mkdir -p ~/.local/share/fonts/ibm-plex-sans

# Extract fonts
unzip ibm-plex-sans.zip -d ~/.local/share/fonts/ibm-plex-sans

# Refresh font cache
fc-cache -f -v

# Verify installation
fc-list | grep "IBM Plex Sans"
```

### Using Custom Fonts

To use a different IBM Plex Sans variant:

```bash
# CLI
ibmdiagrams -font "IBM Plex Sans JP" cloud.tfstate

# Python API
with Diagram("my-diagram", font="IBM Plex Sans JP"):
    pass
```

---

## Verification

### Verify Installation

```bash
# Check version
ibmdiagrams --version

# Show help
ibmdiagrams --help

# Test with example (using uv)
uv run python docs/examples/slzvsi.py

# Test with example (using pip)
python docs/examples/slzvsi.py
```

### Verify Fonts

1. Open draw.io desktop
2. Create a new diagram
3. Add a text box
4. Set font to "IBM Plex Sans"
5. Type: "The quick brown fox jumps over the lazy dog"
6. Verify the font renders correctly (lowercase "l" has slight right bend)

### Run Example Diagram

```bash
# Create a test file
cat > test-diagram.py << 'EOF'
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC
from ibmdiagrams.ibmcloud.compute import VirtualServer

with Diagram("test"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Test VPC"):
                vsi = VirtualServer("Test Server")
EOF

# Run it
python test-diagram.py

# Open the output
open test.drawio  # macOS
start test.drawio  # Windows
xdg-open test.drawio  # Linux
```

---

## Troubleshooting

### Common Issues

<details>
<summary><b>Issue: Command not found: ibmdiagrams</b></summary>

**Symptoms:**
```bash
$ ibmdiagrams --help
bash: ibmdiagrams: command not found
```

**Solutions:**

1. **Using uv**: Run with `uv run ibmdiagrams` instead
   ```bash
   uv run ibmdiagrams cloud.tfstate
   ```

2. **Using pip**: Add Python's bin directory to PATH
   ```bash
   # macOS/Linux - Add to ~/.bashrc or ~/.zshrc
   export PATH="$HOME/.local/bin:$PATH"
   
   # Windows - Add to System Environment Variables
   # C:\Users\<username>\AppData\Local\Programs\Python\Python311\Scripts
   ```

3. **Verify installation location**
   ```bash
   pip show ibmdiagrams
   ```

</details>

<details>
<summary><b>Issue: Import errors when running Python scripts</b></summary>

**Symptoms:**
```python
ModuleNotFoundError: No module named 'ibmdiagrams'
```

**Solutions:**

1. **Using uv**: Run with `uv run python`
   ```bash
   uv run python my-diagram.py
   ```

2. **Using pip**: Activate virtual environment
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Verify installation**
   ```bash
   python -c "import ibmdiagrams; print(ibmdiagrams.__version__)"
   ```

</details>

<details>
<summary><b>Issue: Fonts not rendering correctly in draw.io</b></summary>

**Symptoms:**
- Text appears in default font instead of IBM Plex Sans
- Lowercase "l" looks like "I" (no right bend)

**Solutions:**

1. **Install IBM Plex Sans fonts** (see [Font Installation](#font-installation))

2. **Restart draw.io desktop** after installing fonts

3. **Verify font installation**
   ```bash
   # macOS
   fc-list | grep "IBM Plex Sans"
   
   # Windows - Check in Font Settings
   # Settings → Personalization → Fonts
   ```

4. **Use alternative font temporarily**
   ```bash
   ibmdiagrams -font "Arial" cloud.tfstate
   ```

</details>

<details>
<summary><b>Issue: Python version too old</b></summary>

**Symptoms:**
```bash
ERROR: Python 3.11 or higher is required
```

**Solutions:**

1. **Install Python 3.11+**
   - macOS: `brew install python@3.11`
   - Windows: Download from [python.org](https://www.python.org/downloads/)
   - Linux: `sudo apt install python3.11`

2. **Use uv (automatically manages Python versions)**
   ```bash
   uv sync  # Installs correct Python version automatically
   ```

</details>

<details>
<summary><b>Issue: Permission denied when installing</b></summary>

**Symptoms:**
```bash
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

**Solutions:**

1. **Use user installation** (recommended)
   ```bash
   pip install --user ibmdiagrams-*.whl
   ```

2. **Use virtual environment** (best practice)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install ibmdiagrams-*.whl
   ```

3. **Use uv** (handles permissions automatically)
   ```bash
   uv sync
   ```

</details>

<details>
<summary><b>Issue: draw.io won't open .drawio files</b></summary>

**Symptoms:**
- Double-clicking .drawio files doesn't open draw.io
- Files open in text editor instead

**Solutions:**

1. **Set draw.io as default application**
   - **macOS**: Right-click file → Get Info → Open with → draw.io → Change All
   - **Windows**: Right-click file → Open with → Choose another app → draw.io → Always use
   - **Linux**: Right-click file → Properties → Open With → draw.io → Set as default

2. **Open manually**
   ```bash
   # macOS
   open -a "draw.io" diagram.drawio
   
   # Windows
   "C:\Program Files\draw.io\draw.io.exe" diagram.drawio
   
   # Linux
   drawio diagram.drawio
   ```

</details>

---

## Command Comparison

Quick reference for uv vs pip commands:

| Task | uv | pip |
|------|-----|-----|
| Install dependencies | `uv sync` | `pip install -r requirements.txt` |
| Run script | `uv run python script.py` | `python script.py` |
| Run CLI | `uv run ibmdiagrams file.tfstate` | `ibmdiagrams file.tfstate` |
| Install package | `uv pip install package` | `pip install package` |
| Create environment | Automatic with `uv sync` | `python -m venv venv` |
| Activate environment | Not needed with `uv run` | `source venv/bin/activate` |

---

## Next Steps

Now that you're set up:

1. 📖 **[Getting Started Guide](../GETTING_STARTED.md)** - Create your first diagram
2. 📝 **[Diagram as Code](diagram-as-code.md)** - Learn the Python API
3. 🔄 **[Terraform Guide](terraform.md)** - Generate diagrams from Terraform
4. 📚 **[Examples](examples/)** - Explore real-world diagrams

---

## Additional Resources

- **IBM Design Language**: [Technical Diagrams Guideline](https://www.ibm.com/design/language/infographics/technical-diagrams/design)
- **draw.io Documentation**: [draw.io Help](https://www.drawio.com/doc/)
- **Python Virtual Environments**: [venv Documentation](https://docs.python.org/3/library/venv.html)
- **uv Documentation**: [uv Guide](https://github.com/astral-sh/uv)

---

## License

This application is licensed under the Apache License, Version 2.0. Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
