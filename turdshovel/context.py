import os
from copy import copy
from typing import Any, List, Tuple

from nubia import context, eventbus
from nubia.internal import cmdloader
from nubia.internal.cmdbase import AutoCommand
from pygments.token import Name, Token
from rich import box, inspect
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from sortedcontainers import SortedSet

from ._nubia import _Exit, _Help
from .constants import COMMAND_PACKAGES, NUBIA_OPTIONS, TITLE_ASCII, TITLE_TEXT


class TurdshovelContext(context.Context):
    """Context for the Turdshovel app. Only allows interactive mode"""

    # Need to set this to allow initialization
    available_obj_types = SortedSet()

    def get_prompt_tokens(self) -> List[Tuple[Any, str]]:
        tokens = [
            (Token.NewLine, "\n"),
            (Token.Title, "Turdshovel"),
            (Token.Space, ""),
            (Token.Pound, "> "),
        ]
        if self.target_friendly_name:
            tokens.insert(3, (Name.Command, self.target_friendly_name))
            tokens.insert(3, (Token.At, "@"))

        return tokens

    def _replace_internal_cmds(self, override: bool):
        for k, v in copy(self._registry._cmd_instance_map).items():
            if v.__module__.startswith("nubia.internal.commands"):
                self._registry._cmd_instance_map.pop(k)
                self._registry._completer.meta_dict.pop(k)
                self._registry._completer.words.remove(k)

        # Readd commands for exit and help with less aliases
        for cmd in [_Exit, _Help]:
            self._registry.register_command(cmd(), override)

    def reload_commands(self):
        """Reloads all the commands for the context"""

        self._replace_internal_cmds(override=True)
        for cmd in cmdloader.load_commands(COMMAND_PACKAGES):
            self._registry.register_command(
                AutoCommand(cmd, NUBIA_OPTIONS), override=True
            )

    def on_interactive(self, args):

        self.verbose = args.verbose
        self.console = Console(soft_wrap=True)
        self.console.set_alt_screen()

        # This will be whatever the DataTarget is connected to and the related runtime
        self.target = None
        self.target_friendly_name = ""
        self.runtime = None
        self.available_obj_types = SortedSet()

        title_panel = Panel.fit(
            Text(TITLE_ASCII.rjust(33), style="bold #52311A", end="").append(
                TITLE_TEXT, style="bold #693F21"
            ),
            border_style="bold #52311A",
            subtitle=f"{':poop:' * 36}",
            box=box.SIMPLE,
        )

        self.console.print(Align.center(title_panel))

        self._replace_internal_cmds(override=False)
        self.registry.dispatch_message(eventbus.Message.CONNECTED)
