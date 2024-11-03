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

## Install

1. Download wheel from Releases.
2. pip install ibmdiagrams-x.y.z-py3-none-anywhl where x.y.z refers to the version number.
3. Package is installed to /Library/Frameworks/Python.framework/Versions/VERSION/pythonVERSION/site-packages/ibmdiagrams
4. Script is installed to /Library/Frameworks/Python.framework/Versions/VERSION/bin

<!--
## Build

1. cd ibmdiagrams
2. Update version number in pyproject.toml.
3. python -m build
4. Output is in dist
-->

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
