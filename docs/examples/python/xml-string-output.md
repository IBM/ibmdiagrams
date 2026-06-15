# Getting XML String Output (No File Writing)

This example demonstrates how to generate Draw.io XML as a string without writing to a file.

## Overview

The `getXMLString()` method allows you to:
- Generate diagrams dynamically without file I/O
- Return XML via HTTP APIs
- Store diagrams in databases
- Process diagrams in-memory
- Stream diagrams to clients

## Key Technique

Use `filename="*"` when creating a diagram to prevent automatic file writing:

```python
with Diagram("my-diagram", filename="*"):
    # ... diagram code ...
```

## Complete Example

See [`xml-string-output.py`](xml-string-output.py) for a complete working example.

## Step-by-Step Guide

### 1. Import Required Modules

```python
from ibmdiagrams import _data, _savediagrams
from ibmdiagrams.ibmbase.build import Build
from ibmdiagrams.ibmbase.common import Common
from ibmdiagrams.ibmcloud.diagram import Diagram
# ... other imports ...
```

### 2. Create Diagram with `filename="*"`

```python
with Diagram("my-cloud-architecture", filename="*"):
    with IBMCloud("IBM Cloud"):
        with Region("Dallas"):
            with VPC("Production VPC"):
                # ... diagram components ...
```

### 3. Get XML String After Diagram Creation

```python
# Setup Common and Build instances
common = Common()
common.setInputPython()
build = Build(common, _data)

# Access saved diagram data
if "my-cloud-architecture" in _savediagrams:
    xmldata = _savediagrams["my-cloud-architecture"]
    
    # Get XML as string
    xml_string = build.getXMLString(xmldata, "my-cloud-architecture")
```

## Use Cases

### HTTP API Response

```python
from flask import Flask, Response

app = Flask(__name__)

@app.route('/diagram')
def get_diagram():
    xml_string = create_diagram_get_xml()
    return Response(xml_string, mimetype='application/xml')
```

### Database Storage

```python
import sqlite3

def save_diagram_to_db(diagram_name, xml_string):
    conn = sqlite3.connect('diagrams.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO diagrams (name, xml_content) VALUES (?, ?)",
        (diagram_name, xml_string)
    )
    conn.commit()
    conn.close()
```

### In-Memory Processing

```python
from xml.etree import ElementTree as ET

def process_diagram_xml(xml_string):
    root = ET.fromstring(xml_string)
    # Process XML structure
    return root
```

## Important Notes

1. **No File Created**: Using `filename="*"` prevents any `.drawio` file from being created
2. **Memory Only**: The diagram exists only in memory until you explicitly save it
3. **Access Pattern**: You must access `_savediagrams` after the diagram context exits
4. **Diagram Name**: The key in `_savediagrams` matches the diagram name you provided

## Comparison: File vs String Output

| Feature | Standard (File) | XML String (No File) |
|---------|----------------|---------------------|
| File Created | ✓ Yes | ✗ No |
| Memory Usage | Lower | Higher |
| API Friendly | ✗ No | ✓ Yes |
| Database Storage | Manual | Direct |
| Dynamic Generation | Slower | Faster |

## Running the Example

```bash
# Run the example
python docs/examples/python/xml-string-output.py

# Output will show:
# - XML generation confirmation
# - XML length
# - First 500 characters of XML
# - Suggested use cases
```

## Related Documentation

- [Diagram as Code](../../diagram-as-code.md) - Main diagram creation guide
- [Simple VPC Example](simple-vpc.md) - Basic diagram example
- [SLZ VSI Example](slzvsi.md) - Complex diagram example

## API Reference

### `Build.getXMLString(xmldata, diagram_name)`

Converts diagram data to Draw.io XML string without writing to file.

**Parameters:**
- `xmldata` (dict): The diagram data structure from `_savediagrams`
- `diagram_name` (str): Name of the diagram

**Returns:**
- `str`: Draw.io XML as a string

**Example:**
```python
xml_string = build.getXMLString(xmldata, "my-diagram")