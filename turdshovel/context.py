import os
from copy import copy
from typing import Any, List, Tuple

from nubia import context, eventbus
from pygments.token import Name, Token
from rich import box, inspect
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from ._nubia import _Exit, _Help
from .constants import TITLE_ASCII, TITLE_TEXT


class TurdshovelContext(context.Context):
    """Context for the Turdshovel app. Only allows interactive mode"""

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

    def on_interactive(self, args):
        # os.system("cls||clear")

        self.verbose = args.verbose
        self.console = Console(soft_wrap=True)
        self.console.set_alt_screen()

        # This will be whatever the DataTarget is connected to and the related runtime
        self.target = None
        self.target_friendly_name = ""
        self.runtime = None

        title_panel = Panel.fit(
            Text(TITLE_ASCII.rjust(33), style="bold #52311A", end="").append(
                TITLE_TEXT, style="bold #693F21"
            ),
            border_style="bold #52311A",
            subtitle=f"{':poop:' * 36}",
            box=box.SIMPLE,
        )

        self.console.print(Align.center(title_panel))

        # Make copy of commands and remove the builtins from original list and completers
        for k, v in copy(self._registry._cmd_instance_map).items():
            if v.__module__.startswith("nubia.internal.commands"):
                self._registry._cmd_instance_map.pop(k)
                self._registry._completer.meta_dict.pop(k)
                self._registry._completer.words.remove(k)

        # Readd commands for exit and help with less aliases
        for cmd in [_Exit, _Help]:
            self._registry.register_command(cmd())

        self.registry.dispatch_message(eventbus.Message.CONNECTED)
