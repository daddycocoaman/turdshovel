from rich import box
from rich.align import Align
from rich.panel import Panel
from textual.widget import Widget
from textual_inputs import TextInput as _TextInput


class Title(Widget):
    def __init__(self, label: str, name: str | None = None) -> None:
        self.label = label
        super().__init__(name)

    def render(self) -> Panel:
        return Panel(
            Align.center(self.label, style="bold #0085a8"),
            border_style="#0085a8",
            box=box.HEAVY,
        )


class TextInput(_TextInput):
    border_style = "#0085a8"
