from rich.color import Color
from rich.console import RenderableType
from rich.style import Style
from textual.scrollbar import ScrollBar, ScrollBarRender


class TurdshovelScrollBar(ScrollBar):
    def render(self) -> RenderableType:
        style = Style(
            bgcolor=(Color.parse("#0c2567" if self.mouse_over else "#0b1456")),
            color=Color.parse("#927200" if self.grabbed else "#00485b"),
        )
        return ScrollBarRender(
            virtual_size=self.virtual_size,
            window_size=self.window_size,
            position=self.position,
            vertical=self.vertical,
            style=style,
        )
