"""Tests for core Options and Common wrapper behavior."""

from ibmdiagrams.ibmbase.common import Common
from ibmdiagrams.ibmbase.options import Directions, Options, Providers


def test_options_get_input_folder_returns_input_folder():
    """Options.getInputFolder returns the configured input folder."""
    options = Options()
    options.setInputFolder("input-folder")
    options.setOutputFile("diagram.drawio")

    assert options.getInputFolder() == "input-folder"


def test_common_set_provider_any_delegates_to_options():
    """Common.setProviderAny switches the wrapped Options provider to ANY."""
    common = Common()

    common.setProviderAny()

    assert common.getProvider() == Providers.ANY
    assert common.isProviderAny()


def test_common_get_direction_returns_options_direction():
    """Common.getDirection returns the direction from the wrapped Options object."""
    common = Common()
    common.setDirectionTB()

    assert common.getDirection() == Directions.TB


def test_common_table_folder_wrapper_delegates_to_options():
    """Common table folder accessors use the wrapped Options object."""
    common = Common()

    common.setTablesFolder("tables")

    assert common.getTablesFolder() == "tables"


def test_options_icon_accessors_store_values():
    """Options icon accessors store configured values on the instance."""
    options = Options()
    icons = {"Virtual Server Icon": "enabled"}

    options.setIcons(icons)
    options.setOutputIcons("icons.drawio")

    assert options.getIcons() == icons
    assert options.getOutputIcons() == "icons.drawio"


def test_options_designated_vpc_defaults_to_unrestricted():
    """No configured VPC filter means every VPC name is considered designated."""
    options = Options()

    assert options.isDesignatedVPC("any-vpc")
