from functools import lru_cache
from time import time
from typing import Tuple

from rich.console import RenderableType
from rich.text import Text
from textual.widgets._directory_tree import (
    DirectoryTree,
    DirEntry,
    FileClick,
    NodeID,
    TreeClick,
    TreeNode,
)


class DoubleClickDirectoryTree(DirectoryTree):
    """Instance of DirectoryTree requiring double click to open files"""

    def __init__(self, path: str, name: str = None) -> None:

        # Set the time to -2 seconds to avoid meeting immediate double click condition
        self.last_file_click: Tuple[float, DirEntry] = (
            time() - 2,
            DirEntry(None, False),
        )
        super().__init__(path, name)

    async def watch_hover_node(self, hover_node: NodeID) -> None:
        for node in self.nodes.values():
            node.tree.guide_style = (
                "bold not dim #9e0700" if node.id == hover_node else "black"
            )
        self.refresh(layout=True)

    @lru_cache(maxsize=1024 * 32)
    def render_tree_label(
        self,
        node: TreeNode[DirEntry],
        is_dir: bool,
        expanded: bool,
        is_cursor: bool,
        is_hover: bool,
        has_focus: bool,
    ) -> RenderableType:
        meta = {
            "@click": f"click_label({node.id})",
            "tree_node": node.id,
            "cursor": node.is_cursor,
        }
        label = Text(node.label) if isinstance(node.label, str) else node.label
        if is_hover:
            label.stylize("underline")
        if is_dir:
            label.stylize("bold #0085a8")
            icon = "📂" if expanded else "📁"
        else:
            label.stylize("#c59b00")
            icon = "📄"
            label.highlight_regex(r"\..*$", "#c59b00")

        if label.plain.startswith("."):
            label.stylize("dim")

        if is_cursor and has_focus:
            label.stylize("reverse")

        icon_label = Text(f"{icon} ", no_wrap=True, overflow="ellipsis") + label
        icon_label.apply_meta(meta)
        return icon_label

    async def handle_tree_click(self, message: TreeClick[DirEntry]) -> None:
        dir_entry = message.node.data
        if not dir_entry.is_dir:

            # Get the current time and file entry
            current_click = (time(), dir_entry)

            # If the time difference is less than 1.5 seconds, it's a "double click"
            if (
                current_click[0] - self.last_file_click[0] < 1.5
                and current_click[1] == self.last_file_click[1]
            ):
                await self.emit(FileClick(self, dir_entry.path))

            self.last_file_click = current_click
        else:
            if not message.node.loaded:
                await self.load_directory(message.node)
                await message.node.expand()
            else:
                await message.node.toggle()
