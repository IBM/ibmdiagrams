# Setup

## Prereqs

1. Install Python (3.11.3+):
- Install [Python](https://www.python.org/downloads/).
- After installation the installer will open the install directory.
- Run Update Shell Profile.command to create .zprofile with Python in PATH.
- Add alias python="python3" to .zprofile.
2. Install PIP:
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py
3. (Temporary) For non-static icons, download and install ibm2beta3 drawio desktop (Mac only) from Releases.

## Install

1. Download wheel from Releases.
2. pip install drawit*.whl
3. Package is installed to /Library/Frameworks/Python.framework/Versions/VERSION/pythonVERSION/site-packages/ibmdiagrams
4. Script is installed to /Library/Frameworks/Python.framework/Versions/VERSION/bin

## Build

1. cd ibmdiagrams
2. Update version number in pyproject.toml.
3. python -m build
4. Output is in dist

## Tests

1. cd tests/python
2. Run python on each example.
3. Output is local drawio file.
4. cd tests/terraform
5. ibmdiagrams example.tfstate
6. Output is local drawio file unless -output folder is specified.
7. cd tests/json
8. ibmdiagrams example.json
9. Output is local drawio file unless -output folder is specified.

## Tools

1. Save stencilsrepo/drawio/stencils/2.0/ibm_all_in_one.xml to ibmdiagrams/tools/input/ibm_all_in_one.xml
2. Save https://l2fprod.github.io/myarchitecture/drawio.xml to ibmdiagrams/tools/input/ibm_cloud_catalog.xml
3. cd terraform-provider-ibm/ibm/service
4. find . -name "resource_ibm*.go" -print > ibmdiagrams/tools/input/ibm_terraform_resources.txt
5. cd ibmdiagrams/tools
6. python buildicons.py (reads files from input and writes files to output)
7. python buildresources.py (reads file from input and writes file to output)
8. Copy output files to ibmdiagrams/src/ibmdiagrams/ibmbase

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
