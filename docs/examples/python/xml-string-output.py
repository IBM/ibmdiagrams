"""
Example: Getting Draw.io XML as a String (No File Writing)

This example demonstrates how to create a diagram and get the XML output
as a string instead of writing to a file. This is useful for:
- HTTP API responses
- Database storage
- In-memory processing
- Streaming to clients
- Dynamic diagram generation

Key technique: Use filename="*" to prevent automatic file writing.
"""

import logging

from ibmdiagrams import _data, _savediagrams
from ibmdiagrams.ibmbase.build import Build
from ibmdiagrams.ibmbase.common import Common
from ibmdiagrams.ibmcloud.actors import User
from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.connectors import SolidEdge
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import (
    VPC,
    IBMCloud,
    PublicNetwork,
    Region,
    Subnet,
    Zone,
)
from ibmdiagrams.ibmcloud.network import Internet, PublicGateway

logger = logging.getLogger(__name__)


def create_diagram_get_xml():
    """
    Create a diagram and return XML string WITHOUT writing to file.

    Returns:
        str: The Draw.io XML as a string, or None if generation failed
    """

    # Using filename="*" prevents automatic file writing
    with Diagram("my-cloud-architecture", filename="*"):
        with PublicNetwork("Public Network"):
            user = User("User")
            internet = Internet("Internet")

        with IBMCloud("IBM Cloud"):
            with Region("Dallas"):
                with VPC("Production VPC"):
                    with Zone("Zone 1", "10.10.0.0/18"):
                        pgw = PublicGateway("Public Gateway")
                        with Subnet("Web Tier", "10.10.10.0/24"):
                            vsi1 = VirtualServer("Web Server 1", "10.10.10.4")
                        with Subnet("App Tier", "10.10.20.0/24"):
                            vsi2 = VirtualServer("App Server 1", "10.10.20.4")

        # Connect components
        user - SolidEdge(startarrow="arrow", endarrow="arrow") - internet
        internet - SolidEdge(startarrow="arrow", endarrow="arrow") - pgw
        pgw - SolidEdge(startarrow="arrow", endarrow="none") - vsi1
        vsi1 - SolidEdge(startarrow="arrow", endarrow="arrow") - vsi2

    # After diagram context exits, get the XML string
    common = Common()
    common.setInputPython()
    build = Build(common, _data)

    # Access the saved diagram data
    if "my-cloud-architecture" in _savediagrams:
        xmldata = _savediagrams["my-cloud-architecture"]

        # Convert to XML string - NO FILE WRITING!
        xml_string = build.getXMLString(xmldata, "my-cloud-architecture")
        return xml_string

    return None


def main():
    """Main function demonstrating XML string generation."""
    logger.info("Creating diagram and getting XML string (no file writing)...\n")

    xml_output = create_diagram_get_xml()

    if xml_output:
        logger.info("✓ Successfully generated XML without writing to file!")
        logger.info("XML length: %d characters", len(xml_output))
        logger.info("First 500 characters of XML:")
        logger.info("=" * 80)
        logger.info(xml_output[:500])
        logger.info("=" * 80)

        # Example use cases for the XML string:
        logger.info("📋 Use Cases for XML String:")
        logger.info("  • Send via HTTP API response")
        logger.info("  • Store in database")
        logger.info("  • Process in-memory")
        logger.info("  • Stream to clients")
        logger.info("  • Generate dynamically on-demand")

        # Optional: Write to file if needed
        # with open("output.drawio", "w", encoding="utf-8") as f:
        #     f.write(xml_output)

        return xml_output
    else:
        logger.error("✗ Failed to generate XML")
        return None


if __name__ == "__main__":
    xml = main()
