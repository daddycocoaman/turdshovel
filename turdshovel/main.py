import sys

from nubia import Nubia

from .constants import COMMAND_PACKAGES, NUBIA_OPTIONS
from .plugin import TurdshovelPlugin


def init():
    plugin = TurdshovelPlugin()

    shell = Nubia(
        name="Turdshovel",
        command_pkgs=COMMAND_PACKAGES,
        plugin=plugin,
        options=NUBIA_OPTIONS,
    )
    sys.exit(shell.run())
