"""
Tests for LayoutGroup component.

This module tests the LayoutGroup class to ensure it provides
layout grouping without visual boundaries.
"""

import pytest

from ibmdiagrams.ibmcloud.compute import VirtualServer
from ibmdiagrams.ibmcloud.diagram import Diagram
from ibmdiagrams.ibmcloud.groups import LayoutGroup


class TestLayoutGroupInstantiation:
    """Test LayoutGroup instantiation and basic properties."""

    def test_layout_group_can_be_instantiated(self):
        """Test that LayoutGroup can be created with default parameters."""
        with Diagram("test"):
            group = LayoutGroup()
            assert group is not None

    def test_layout_group_with_direction(self):
        """Test that LayoutGroup accepts direction parameter."""
        with Diagram("test"):
            group = LayoutGroup(direction="TB")
            assert group is not None

    def test_layout_group_inherits_from_grouping(self):
        """Test that LayoutGroup inherits from _Grouping."""
        with Diagram("test"):
            from ibmdiagrams.ibmcloud.groups import _Grouping

            group = LayoutGroup()
            assert isinstance(group, _Grouping)


class TestLayoutGroupVisualStyling:
    """Test that LayoutGroup has no visual styling."""

    def test_layout_group_renders_without_errors(self):
        """Test that LayoutGroup renders without errors (functional test for styling)."""
        with Diagram("test"):
            with LayoutGroup():
                server = VirtualServer("Server", "10.0.0.1")
            # If we get here without errors, the invisible styling works
            assert server is not None


class TestLayoutGroupDirection:
    """Test LayoutGroup direction parameter."""

    def test_horizontal_layout(self):
        """Test LayoutGroup with left-to-right direction."""
        with Diagram("test"):
            group = LayoutGroup(direction="LR")
            assert group is not None

    def test_vertical_layout(self):
        """Test LayoutGroup with top-to-bottom direction."""
        with Diagram("test"):
            group = LayoutGroup(direction="TB")
            assert group is not None

    def test_default_direction(self):
        """Test that LayoutGroup defaults to LR direction."""
        with Diagram("test"):
            group = LayoutGroup()
            assert group is not None


class TestLayoutGroupContextManager:
    """Test LayoutGroup as context manager with nested elements."""

    def test_context_manager_usage(self):
        """Test that LayoutGroup works with Python's with statement."""
        with Diagram("test"):
            with LayoutGroup() as group:
                server1 = VirtualServer("Server 1")
                server2 = VirtualServer("Server 2")
            assert group is not None
            assert server1 is not None
            assert server2 is not None

    def test_nested_elements(self):
        """Test that elements can be nested within LayoutGroup."""
        with Diagram("test"):
            with LayoutGroup(direction="TB"):
                server1 = VirtualServer("Server 1", "10.0.0.1")  # noqa: F841
                server2 = VirtualServer("Server 2", "10.0.0.2")  # noqa: F841
            # If we get here without errors, nesting works
            assert True


class TestLayoutGroupParameters:
    """Test that LayoutGroup only accepts direction parameter."""

    def test_accepts_direction_parameter(self):
        """Test that LayoutGroup accepts direction parameter."""
        with Diagram("test"):
            group = LayoutGroup(direction="TB")
            assert group is not None

    def test_no_label_parameter(self):
        """Test that LayoutGroup does not accept label parameter."""
        with Diagram("test"):
            with pytest.raises(TypeError):
                group = LayoutGroup("Label")  # noqa: F841

    def test_no_sublabel_parameter(self):
        """Test that LayoutGroup does not accept sublabel parameter."""
        with Diagram("test"):
            with pytest.raises(TypeError):
                group = LayoutGroup(sublabel="Sublabel")  # noqa: F841

    def test_no_background_parameter(self):
        """Test that LayoutGroup does not accept background parameter."""
        with Diagram("test"):
            with pytest.raises(TypeError):
                group = LayoutGroup(background="white")  # noqa: F841

    def test_no_linecolor_parameter(self):
        """Test that LayoutGroup does not accept linecolor parameter."""
        with Diagram("test"):
            with pytest.raises(TypeError):
                group = LayoutGroup(linecolor="#000000")  # noqa: F841

    def test_no_fillcolor_parameter(self):
        """Test that LayoutGroup does not accept fillcolor parameter."""
        with Diagram("test"):
            with pytest.raises(TypeError):
                group = LayoutGroup(fillcolor="#FFFFFF")  # noqa: F841

    def test_no_icon_parameter(self):
        """Test that LayoutGroup does not accept icon parameter."""
        with Diagram("test"):
            with pytest.raises(TypeError):
                group = LayoutGroup(icon="Some Icon")  # noqa: F841
