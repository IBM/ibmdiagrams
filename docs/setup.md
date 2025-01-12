# Setup

## Install prereqs

1. Install Python (3.11.3+):
- Install [Python](https://www.python.org/downloads/).
- After installation the installer will open the install directory.
- Run Update Shell Profile.command to create .zprofile with Python in PATH.
- Add alias python="python3" to .zprofile.
2. Install PIP:
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py

## Install ibmdiagrams

1. Download wheel from Releases.
2. pip install ibmdiagrams-x.y.z-py3-none-anywhl where x.y.z refers to the version number.
3. Package is installed to /Library/Frameworks/Python.framework/Versions/VERSION/pythonVERSION/site-packages/ibmdiagrams
4. Script is installed to /Library/Frameworks/Python.framework/Versions/VERSION/bin

## Install IBM Plex Fonts

- IBM Plex Sans fonts:
1. IBM Plex Sans (default)
2. IBM Plex Sans Arabic
3. IBM Plex Sans Devanagari
4. IBM Plex Sans Hebrew
5. IBM Plex Sans JP
6. IBM Plex Sans KR
7. IBM Plex Sans Thai
- Install on Mac for use with drawio desktop:
1. Go to: https://fonts.google.com/?query=Plex
2. Select IBM Plex Sans (or global IBM Plex Sans), select Get font, select Download all.
3. Unpack IBM_Plex_Sans.zip (or global zip).
4. Open Font Book app.
5. Select File, select Add Fonts to Current User, select unpacked folder.
6. Set fontFamily=IBM Plex Sans (or global IBM Plex Sans).
7. For default IBM Plex Sans, verify that a lower case L in a label has a slight right bend at bottom.

<!--
## Build

1. cd ibmdiagrams
2. Update version number in pyproject.toml.
3. python -m build
4. Output is in dist
-->

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
