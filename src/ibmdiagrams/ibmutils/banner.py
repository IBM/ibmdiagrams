# @file banner.py
#
# Copyright contributors to the ibmdiagrams project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

from fastmcp import FastMCP
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

# IBM DIAGRAMS ASCII logo in IBM blue gradient
#
# ████ ██████ ███    ███     ██████ ████ ███████ ██████  ██████  ███████ ███    ███ ███████
#  ██  ██  ██ ████  ████     ██  ██  ██  ██   ██ ██      ██   ██ ██   ██ ████  ████ ██
#  ██  ██████ ██ ████ ██     ██  ██  ██  ███████ ██  ███ ██████  ███████ ██ ████ ██ ███████
#  ██  ██  ██ ██  ██  ██     ██  ██  ██  ██   ██ ██   ██ ██   ██ ██   ██ ██  ██  ██      ██
# ████ ██████ ██      ██     ██████ ████ ██   ██ ███████ ██   ██ ██   ██ ██      ██ ███████
#

LOGO_ASCII = (
    "\x1b[38;2;0;98;255m████ ██████ ███    ███     ██████ ████ ███████ ██████  ██████  ███████ ███    ███ ███████\x1b[39m\n"
    "\x1b[38;2;0;110;255m ██  ██  ██ ████  ████     ██  ██  ██  ██   ██ ██      ██   ██ ██   ██ ████  ████ ██     \x1b[39m\n"
    "\x1b[38;2;0;122;255m ██  ██████ ██ ████ ██     ██  ██  ██  ███████ ██  ███ ██████  ███████ ██ ████ ██ ███████\x1b[39m\n"
    "\x1b[38;2;0;134;255m ██  ██  ██ ██  ██  ██     ██  ██  ██  ██   ██ ██   ██ ██   ██ ██   ██ ██  ██  ██      ██\x1b[39m\n"
    "\x1b[38;2;0;146;255m████ ██████ ██      ██     ██████ ████ ██   ██ ███████ ██   ██ ██   ██ ██      ██ ███████\x1b[39m\n"
)


def log_server_banner(server: FastMCP[Any]) -> None:
    """Creates and logs a formatted banner with server information and logo."""

    # Create the logo text
    # Use Text with no_wrap and markup disabled to preserve ANSI escape codes
    logo_text = Text.from_ansi(LOGO_ASCII, no_wrap=True)

    # Create the main title
    title_text = Text(f"{server.name} v{server.version}", style="bold blue")

    # Create panel with logo, title, and information using Group
    docs_url = Text("https://github.com/IBM/ibmdiagrams", style="dim")
    panel_content = Group(
        "",
        Align.center(logo_text),
        "",
        "",
        Align.center(title_text),
        Align.center(docs_url),
    )

    panel = Panel(
        panel_content,
        border_style="dim",
        padding=(1, 4),
        width=120,  # Set max width for the panel
    )

    console = Console(stderr=True)

    # Build output elements
    output_elements: list[Align | Panel | str] = ["\n", Align.center(panel)]

    output_elements.append("\n")

    console.print(Group(*output_elements))
