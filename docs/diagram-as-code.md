# Diagram as Code

<details><summary>IBM Cloud Parameters</summary>

1. Diagram
- name
- filename
- folder
- direction = "LR" (default, left to right) or "TB" (top to bottom)
2. Grouping Shapes and Expanded Shapes
- label = primary label (SemiBold font)
- sublabel = secondary label (Regular font)
- direction = "LR" (default, left to right) or "TB" (top to bottom)
- fontname = "IBM Plex Sans" (default) or other Plex font
- fontsize = 14 (default) 
3. Collapsed Shapes
- label = primary label (SemiBold font)
- sublabel = secondary label (Regular font)
- fontname = "IBM Plex Sans" (default) or other Plex font
- fontsize = 14 (default) 
4. Connectors
- label = connector label
- startarrow = "" (no arrow), "arrow" (default), "circle", "diamond", "openarrow", "opencircle", "opendiamond"
- endarrow = "" (no arrow), "arrow" (default), "circle", "diamond", "openarrow", "opencircle", "opendiamond"
- fontname = "IBM Plex Sans" (default) or other Plex font
- fontsize = 14 (default) 

</details>

<details><summary>IBM Cloud Types</summary>

1. Connectors (connectors.py)
- Solid Edge
- Provate Solid Edge
- Public Solid Edge
- Dashed Edge
- Dotted Edge
- Double Edge
- Tunnel Edge 

</details>

<details><summary>IBM Shapes (if available) Parameters</summary>

1. Diagram
- name
- filename
- folder
- direction = "LR" (default, left to right) or "TB" (top to bottom)
2. Grouping Shapes and Expanded Shapes
- label = primary label (SemiBold font)
- sublabel = secondary label (Regular font)
- direction = "LR" (default, left to right) or "TB" (top to bottom)
- linecolor = from IBM Color Palette
- fillcolor = from IBM Color Palette
- linewidth = 1 (default) 
- icon = name of icon
- fontname = "IBM Plex Sans" (default) or other Plex font
- fontsize = 14 (default) 
3. Collapsed Shapes
- label = primary label (SemiBold font)
- sublabel = secondary label (Regular font)
- linecolor = from IBM Color Palette
- fillcolor = from IBM Color Palette
- icon = name of icon
- fontname = "IBM Plex Sans" (default) or other Plex font
- fontsize = 14 (default) 
4. Connectors
- label = connector label
- startarrow = "" (no arrow), "arrow" (default), "circle", "diamond", "openarrow", "opencircle", "opendiamond"
- endarrow = "" (no arrow), "arrow" (default), "circle", "diamond", "openarrow", "opencircle", "opendiamond"
- color = from IBM Color Palette
- width = 1 (default) 
- fontname = "IBM Plex Sans" (default) or other Plex font
- fontsize = 14 (default) 

</details>

<details><summary>IBM Shapes (if available) Types</summary>

1. Connectors (connectors.py)
- Solid Edge
- Dashed Edge
- Long Dashed Edge
- Dotted Edge
- Double Edge
- Tunnel Edge 

</details>

<details><summary>Examples</summary>

1. [VSI on VPC Landing Zone](examples/slzvsi.md)
2. [Power Virtual Server with VPC Landing Zone](examples/slzpowervs.md)

</details>

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
