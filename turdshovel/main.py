import sys

from nubia import Nubia, Options

import turdshovel.commands

from .plugin import TurdshovelPlugin


def init():
    plugin = TurdshovelPlugin()

    shell = Nubia(
        name="Turdshovel",
        command_pkgs=turdshovel.commands,
        plugin=plugin,
        options=Options(persistent_history=True, auto_execute_single_suggestions=False),
    )
    sys.exit(shell.run())
