"""
Visual regression tests for complete IBM Cloud diagrams.

This module tests complete, real-world diagram examples to ensure
they render correctly end-to-end.
"""

import logging
from pathlib import Path

import pytest

from utils.image_comparison import (
    ImageComparisonError,
    ImageLoadError,
    ImageSizeMismatchError,
    compare_images,
    compare_images_with_tolerance,
    save_diff_image,
)

logger = logging.getLogger(__name__)


def slzpowervs_diagram_code() -> str:
    """Return the code for the slzpowervs diagram."""
    return '''
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet, CloudServices, PowerWorkspace, ResourceGroup, SecurityGroup, ExpandedVirtualServer, ExpandedPowerVirtualServer
from ibmdiagrams.ibmcloud.actors import User, Application
from ibmdiagrams.ibmcloud.devops import Ansible
from ibmdiagrams.ibmcloud.compute import ImageService, PowerVirtualServer
from ibmdiagrams.ibmcloud.network import DNS, FIP, LB, NTP, NetworkInterface, ProxyServer, PublicGateway, TGW, VPE
from ibmdiagrams.ibmcloud.observability import CloudLogs, FlowLogs
from ibmdiagrams.ibmcloud.security import BastionHost, KeyProtect, SSHKey, VPN
from ibmdiagrams.ibmcloud.storage import BlockStorage, FileStorage, ObjectStorage

with Diagram("slzpowervs"):
  with IBMCloud("IBM Cloud"):
    with Zone("Zone 1", direction="TB"):
      with ResourceGroup("Edge<br>Resource Group"):
        with VPC("Edge VPC", "Default ACL") as vpc:
          with SecurityGroup("Default SG"):
            with Subnet("VPN Subnet", "10.20.10.0/24"):
              vpn = VPN("VPN Gateway", "Client to Site")
          with SecurityGroup("Management SG"):
            with Subnet("Mgmt VSI Subnet", "10.30.20.0/24"):
              with ExpandedVirtualServer("Virtual Server"):
                fip = FIP("Floating IP")
                bastion = BastionHost("Bastion Host")
          with SecurityGroup("VPE SG"):
            with Subnet("VPE Subnet", "10.30.30.0/24"):
              vpe = VPE("VPE Gateway", "COS")
          with SecurityGroup("Network Services SG"):
            with Subnet("Edge VSI Subnet", "10.30.40.0/24"):
              pg = PublicGateway("Public Gateway")
              alb = LB("Application<br>Load Balancer")
              file = FileStorage("File Storage")
              with ExpandedVirtualServer("Virtual Server"):
                proxy = ProxyServer("Proxy Server")
                dns = DNS("DNS Forwarder")
                ntp = NTP("NTP Forwarder")
                ansible = Ansible("Ansible Node")

      tgw = TGW("Transit Gateway")

      with ResourceGroup("PowerVS<br>Resource Group"):
        with PowerWorkspace("Secure PowerVS<br>Workspace") as power:
          sshkey = SSHKey("SSH Public Key")
          images = ImageService("Catalog Stock Images")
          with ExpandedPowerVirtualServer("Power VS") as powervsi:
            mgmtstorage = BlockStorage("Management<br>Block Storage")
            backupstorage = BlockStorage("Backup<br>Block Storage")
          mgmtnic = NetworkInterface("Management veth")
          backupnic = NetworkInterface("Backup veth")
          with Subnet("Management Subnet", "10.51.0.0/24"):
            mgmtsubnet = NetworkInterface("Management<br>Network")
          with Subnet("Backup Subnet", "10.51.0.0/24"):
            backupsubnet = NetworkInterface("Backup<br>Network")
          powervsi - mgmtnic - mgmtsubnet
          powervsi - backupnic - backupsubnet

      tgw - vpc
      tgw - power

      with ResourceGroup("Services<br>Resource Group"):
        with CloudServices("Cloud Services"):
          logs = CloudLogs("Activity Tracker")
          flowlogs = FlowLogs("Edge<br>Flow Log<br>Collector")
          keyprotect = KeyProtect("Key Management")
          objectstorage = ObjectStorage("Object Storage", "Installation Files")
          objectstoragelogs = ObjectStorage("Object Storage", "Activity Tracker")
'''


def cloud_diagram_code() -> str:
    """Return the code for the cloud diagram."""
    return '''
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import IBMCloud, Region, VPC, Zone, Subnet, PublicNetwork, EnterpriseNetwork, ExpandedVirtualServer
from ibmdiagrams.ibmcloud.actors import User
from ibmdiagrams.ibmcloud.network import Internet, PublicGateway, FIP, NetworkLoadBalancer
from ibmdiagrams.ibmcloud.security import VPNConnection, VPNGateway

with Diagram("cloud"):
    with PublicNetwork("Public<br>network", direction="TB"):
        User(label="User")
        Internet(label="Internet")
        VPNConnection("VPN<br>connection")

    with IBMCloud("IBM Cloud"):
        with Region("Dallas Region", direction="TB"):
            with VPC("VPC A"):
                with Zone("Dallas Zone 1", sublabel="10.10.0.0/18", direction="LR"):
                    PublicGateway(label="Public gateway")
                    FIP(label="Floating IP")
                    VPNGateway(label="VPN gateway")

                    with Subnet("Subnet 1", sublabel="10.10.10.0/24"):
                        with ExpandedVirtualServer(
                            label="VSI 1",
                            sublabel="Type: Dedicated",
                        ):
                            pass
                    with Subnet("Subnet 2", sublabel="10.10.20.0/24"):
                        with ExpandedVirtualServer(
                            label="VSI 2",
                            sublabel="Type: Dedicated",
                        ):
                            pass
                        

                NetworkLoadBalancer("Public load<br>balancer")
                NetworkLoadBalancer("Private load<br>balancer")

                with Zone("Dallas Zone 2", sublabel="10.10.0.0/18", direction="TB"):
                    with Subnet("Subnet 3", sublabel="10.10.10.0/24"):
                        with ExpandedVirtualServer(
                            label="VSI 3",
                            sublabel="Type: Dedicated",
                        ):
                            pass
                    with Subnet("Subnet 4", sublabel="10.10.20.0/24"):
                        with ExpandedVirtualServer(
                            label="VSI 4",
                            sublabel="Type: Dedicated",
                        ):
                            pass
                    pass
                pass


    with EnterpriseNetwork("Enterprise<br>network", direction="TB"):
        User(label="Enterprise<br>user")
'''


def generate_complete_diagram(
    diagram_name: str,
    diagram_code: str,
    output_dir: Path,
    drawio_path: Path | None,
) -> Path:
    """
    Generate a complete diagram for testing.

    Args:
        diagram_name: Name of the diagram (used for filenames).
        diagram_code: Python code that generates the diagram.
        output_dir: Directory for output files.
        drawio_path: Path to draw.io executable.

    Returns:
        Path to generated PNG file.

    Raises:
        RuntimeError: If diagram generation fails.
    """
    # Create subdirectories for drawio and png
    drawio_dir = output_dir / "drawio"
    png_dir = output_dir / "png"
    drawio_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)

    # Execute the diagram code to generate .drawio file
    drawio_file = drawio_dir / f"{diagram_name}.drawio"
    
    # Create a temporary Python file and execute it
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(diagram_code)
        temp_py_file = Path(f.name)
    
    try:
        # Execute the diagram generation code
        import subprocess
        import sys
        result = subprocess.run(
            [sys.executable, str(temp_py_file)],
            cwd=drawio_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )
        
        if result.returncode != 0:
            raise RuntimeError(
                f"Failed to generate diagram: {result.stderr}"
            )
        
        # Check if drawio file was created
        if not drawio_file.exists():
            raise RuntimeError(
                f"Diagram file not created: {drawio_file}"
            )
        
        # Convert to PNG using draw.io
        if drawio_path is None:
            raise RuntimeError("draw.io executable not found")
        
        png_file = png_dir / f"{diagram_name}.png"
        
        from utils.baseline_utils import convert_drawio, PNG_SCALE, PNG_QUALITY
        convert_drawio(
            drawio_file,
            png_file,
            fmt="png",
            drawio_path=drawio_path,
            scale=PNG_SCALE,
            quality=PNG_QUALITY,
        )
        
        if not png_file.exists():
            raise RuntimeError(f"PNG file not created: {png_file}")
        
        return png_file
        
    finally:
        # Clean up temporary file
        temp_py_file.unlink(missing_ok=True)


@pytest.mark.visual_regression
@pytest.mark.threshold(1.0)  # Allow 1% difference for complex diagrams
def test_slzpowervs_diagram(
    temp_output_dir: Path,
    test_threshold: float,
    pixel_tolerance: int,
    update_baselines: bool,
    save_diffs: bool,
    diff_output_dir: Path,
    drawio_executable: Path | None,
) -> None:
    """
    Test that the slzpowervs complete diagram renders correctly.

    This test generates the full slzpowervs diagram and compares it with
    the baseline image.

    Args:
        temp_output_dir: Temporary directory for test outputs.
        test_threshold: Maximum allowed difference percentage.
        pixel_tolerance: Per-pixel color tolerance.
        update_baselines: If True, update baselines instead of comparing.
        save_diffs: If True, save diff images on failure.
        diff_output_dir: Directory for saving diff images.
        drawio_executable: Path to draw.io executable.
    """
    # Skip if draw.io not available
    if drawio_executable is None:
        pytest.skip(
            "draw.io executable not found. "
            "Install from: https://github.com/jgraph/drawio-desktop/releases"
        )

    diagram_name = "slzpowervs"
    baseline_dir = Path(__file__).parent / "baselines"
    baseline_png_dir = baseline_dir / "png"
    baseline_png = baseline_png_dir / f"{diagram_name}.png"

    # Check baseline exists
    if not baseline_png.exists() and not update_baselines:
        pytest.fail(
            f"Baseline image not found: {baseline_png}\n"
            f"Run with --update-baselines to generate baseline."
        )

    # Generate test diagram
    try:
        generated_png = generate_complete_diagram(
            diagram_name,
            slzpowervs_diagram_code(),
            temp_output_dir,
            drawio_executable,
        )
    except Exception as e:
        pytest.fail(f"Failed to generate diagram: {e}")

    # Update baseline mode
    if update_baselines:
        baseline_png_dir.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy2(generated_png, baseline_png)
        logger.info(f"Updated baseline: {baseline_png}")
        pytest.skip(f"Baseline updated: {baseline_png}")
        return

    # Compare images
    try:
        if pixel_tolerance > 0:
            is_match, diff_percentage, diff_image = compare_images_with_tolerance(
                baseline_png,
                generated_png,
                threshold=test_threshold,
                pixel_tolerance=pixel_tolerance,
            )
        else:
            is_match, diff_percentage, diff_image = compare_images(
                baseline_png,
                generated_png,
                threshold=test_threshold,
            )

        if not is_match:
            # Save diff image if requested
            if save_diffs and diff_image is not None:
                diff_path = diff_output_dir / f"{diagram_name}_diff.png"
                save_diff_image(diff_image, diff_path)
                diff_msg = f"\n  Diff image: {diff_path}"
            else:
                diff_msg = "\n  Run with --save-diffs to generate diff image"

            pytest.fail(
                f"\nVisual regression test failed for diagram: {diagram_name}\n"
                f"  Difference: {diff_percentage:.2f}%\n"
                f"  Threshold: {test_threshold:.2f}%{diff_msg}\n\n"
                f"The generated diagram differs from the baseline by {diff_percentage:.2f}%.\n"
                f"This exceeds the allowed threshold of {test_threshold:.2f}%.\n\n"
                f"If this change is intentional:\n"
                f"  1. Review the visual changes carefully\n"
                f"  2. Run: pytest {__file__} --update-baselines\n"
                f"  3. Commit the updated baseline image"
            )

        logger.info(
            f"Visual regression test passed for {diagram_name}: "
            f"{diff_percentage:.2f}% difference (threshold: {test_threshold:.2f}%)"
        )

    except ImageSizeMismatchError as e:
        pytest.fail(
            f"\nImage dimensions don't match for {diagram_name}:\n"
            f"  {e}\n\n"
            f"This usually indicates a significant change in diagram generation.\n"
            f"If this change is intentional, update the baseline:\n"
            f"  pytest {__file__} --update-baselines"
        )
    except (ImageLoadError, ImageComparisonError) as e:
        pytest.fail(f"Image comparison failed for {diagram_name}: {e}")


@pytest.mark.visual_regression
@pytest.mark.threshold(1.0)  # Allow 1% difference for complex diagrams
def test_cloud_diagram(
    temp_output_dir: Path,
    test_threshold: float,
    pixel_tolerance: int,
    update_baselines: bool,
    save_diffs: bool,
    diff_output_dir: Path,
    drawio_executable: Path | None,
) -> None:
    """
    Test that the cloud complete diagram renders correctly.

    This test generates the full cloud diagram and compares it with
    the baseline image.

    Args:
        temp_output_dir: Temporary directory for test outputs.
        test_threshold: Maximum allowed difference percentage.
        pixel_tolerance: Per-pixel color tolerance.
        update_baselines: If True, update baselines instead of comparing.
        save_diffs: If True, save diff images on failure.
        diff_output_dir: Directory for saving diff images.
        drawio_executable: Path to draw.io executable.
    """
    # Skip if draw.io not available
    if drawio_executable is None:
        pytest.skip(
            "draw.io executable not found. "
            "Install from: https://github.com/jgraph/drawio-desktop/releases"
        )

    diagram_name = "cloud"
    baseline_dir = Path(__file__).parent / "baselines"
    baseline_png_dir = baseline_dir / "png"
    baseline_png = baseline_png_dir / f"{diagram_name}.png"

    # Check baseline exists
    if not baseline_png.exists() and not update_baselines:
        pytest.fail(
            f"Baseline image not found: {baseline_png}\n"
            f"Run with --update-baselines to generate baseline."
        )

    # Generate test diagram
    try:
        generated_png = generate_complete_diagram(
            diagram_name,
            cloud_diagram_code(),
            temp_output_dir,
            drawio_executable,
        )
    except Exception as e:
        pytest.fail(f"Failed to generate diagram: {e}")

    # Update baseline mode
    if update_baselines:
        baseline_png_dir.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy2(generated_png, baseline_png)
        logger.info(f"Updated baseline: {baseline_png}")
        pytest.skip(f"Baseline updated: {baseline_png}")
        return

    # Compare images
    try:
        if pixel_tolerance > 0:
            is_match, diff_percentage, diff_image = compare_images_with_tolerance(
                baseline_png,
                generated_png,
                threshold=test_threshold,
                pixel_tolerance=pixel_tolerance,
            )
        else:
            is_match, diff_percentage, diff_image = compare_images(
                baseline_png,
                generated_png,
                threshold=test_threshold,
            )

        if not is_match:
            # Save diff image if requested
            if save_diffs and diff_image is not None:
                diff_path = diff_output_dir / f"{diagram_name}_diff.png"
                save_diff_image(diff_image, diff_path)
                diff_msg = f"\n  Diff image: {diff_path}"
            else:
                diff_msg = "\n  Run with --save-diffs to generate diff image"

            pytest.fail(
                f"\nVisual regression test failed for diagram: {diagram_name}\n"
                f"  Difference: {diff_percentage:.2f}%\n"
                f"  Threshold: {test_threshold:.2f}%{diff_msg}\n\n"
                f"The generated diagram differs from the baseline by {diff_percentage:.2f}%.\n"
                f"This exceeds the allowed threshold of {test_threshold:.2f}%.\n\n"
                f"If this change is intentional:\n"
                f"  1. Review the visual changes carefully\n"
                f"  2. Run: pytest {__file__} --update-baselines\n"
                f"  3. Commit the updated baseline image"
            )

        logger.info(
            f"Visual regression test passed for {diagram_name}: "
            f"{diff_percentage:.2f}% difference (threshold: {test_threshold:.2f}%)"
        )

    except ImageSizeMismatchError as e:
        pytest.fail(
            f"\nImage dimensions don't match for {diagram_name}:\n"
            f"  {e}\n\n"
            f"This usually indicates a significant change in diagram generation.\n"
            f"If this change is intentional, update the baseline:\n"
            f"  pytest {__file__} --update-baselines"
        )
    except (ImageLoadError, ImageComparisonError) as e:
        pytest.fail(f"Image comparison failed for {diagram_name}: {e}")
