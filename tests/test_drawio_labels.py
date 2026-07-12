"""Regression tests for DrawIO label rendering."""

from pathlib import Path

from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import VPC, IBMCloud, Region, Subnet, Zone


def test_drawio_labels_are_not_truncated(tmp_path: Path):
    with Diagram("long-labels", output=str(tmp_path)):
        with IBMCloud("IBM Cloud with a long name"):
            with Region("Dallas"):
                with VPC("My Production VPC with a long name"):
                    with Zone("Zone 1", "10.10.0.0/18"):
                        with Subnet("App Subnet", "10.10.10.0/24"):
                            VirtualServer("Web Server", "10.10.10.4")

    drawio = (tmp_path / "long-labels.drawio").read_text(encoding="utf-8")

    assert "IBM Cloud with a long name" in drawio
    assert "My Production VPC with a long name" in drawio
    assert "IBM Cloud with..." not in drawio
    assert "My Production ..." not in drawio
