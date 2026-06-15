# Using JSON (tooling)

## Overview

IBM Diagrams supports an internal JSON format for diagram generation. This format is primarily for internal use and advanced integrations.

⚠️ **Note:** This format is subject to change and not recommended for production use. Use the [Python API](diagram-as-code.md) or [Terraform integration](terraform.md) instead.

## Usage

```bash
# Generate diagram from JSON file
ibmdiagrams docs/examples/json/cloud.json

# Output: cloud.drawio (created in current directory)
```

## Examples

See the [examples/json](examples/json/) directory for sample JSON files and detailed documentation.

## JSON Format

The JSON format expects a resource-based structure with `vpcs`, `subnets`, and `instances` at the top level. See [examples/json/README.md](examples/json/README.md) for the complete format specification and examples.

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
