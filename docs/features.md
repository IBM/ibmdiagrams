# ibmdiagrams Features

ibmdiagrams generated architecture diagrams following IBM Diagram Standard.
## Features

1. Shapes:
- Group (container group) represents a deployedOn relationship.  
- Zone (non-container group) represents a deployedTo relationship. 
- Node (square shape) represent standalone components or devices.
- Actor (round shape) represent roles, functions or attributes played by human users, devices and other entities that interact with any of the above.

2. Naming Conventions
- IBM (except for IBM Cloud), VPC (default), and conjunctions in product names are simplified in Python: Virtual Server for VPC is VirtualServer in Python, Bare Metal Server for VPC is BareMetalServer in Python, Virtual Server for Classic is ClassicVirtualServer in Python, Bare Metal Server for Classic is ClassicBareMetalServer in Python.
- Aliases also help simplify names: Availability Zone has alias of Zone so either name can be used. 

3. deployedOn vs deployedTo
- deployedOn (container=1) specifies where services and applications are deployed, e.g. virtual server is `deployedOn` a subnet.
- deployedTo (container=0) specifies where an application, service, or component is deployed to, e.g. a virtual server is `deployedTo` a security group.

4. Input Options
- Python - Create diagrams from Python code for non-provisioned infrastructure.  
- Terraform - Create diagrams from provisioned infrastructure created by Terraform.

5. Output Options
- Static Icons - icons available from the [external repo](https://github.com/IBM-Cloud/architecture-icons) for use in any drawio desktop. 

6. Selecting within non-containers
- ibmdiagrams generates correct Z order autommatically.
- If needed, use alt-click or option-click to select shapes, or define Z order by moving shapes backward.

7. Labels
- ibmdiagrams enables the use of two labels on all shapes with a label that is SemiBold font and a sublabel (under label) with regular font.

8. Fill colors
- ibmdiagrams generates shapes with fill colors that are either white or the light color from the same color family as the corresponding primary color. For example, Cyan 50 is a primary color and the corresponding fill color is either white or Cyan 10 for accessibility.
- ibmdiagrams alternates between white and light fill for consecutive nested groups for accessibility.

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
