from pathlib import Path

import typer
from Microsoft.Diagnostics.Runtime import ClrRuntime
from textual.app import App
from textual.widgets import FileClick, ScrollView, Static
from textual_inputs.events import Message

from turdshovel.widgets.assembly import AssemblyInstanceTree, AssemblyTree
from turdshovel.widgets.directorytree import DoubleClickDirectoryTree
from turdshovel.widgets.dump import DumpFile
from turdshovel.widgets.footer import TurdshovelFooter
from turdshovel.widgets.header import TextInput, Title
from turdshovel.widgets.scrollbar import TurdshovelScrollBar

cli_app = typer.Typer(name="Turdshovel", short_help="Digging through dumps for gold")


class Turdshovel(App):
    """Turdshovel application"""

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("q", "quit", "Quit")

    async def on_mount(self):

        self._dump_summary = None
        self.runtime: ClrRuntime = None

        # Add the footer
        self.footer = TurdshovelFooter()
        await self.view.dock(self.footer, edge="bottom")

        # Create grid area for title, directory tree, and summary field
        self.grid = await self.view.dock_grid()
        self.grid.add_column(name="info", size=30)
        self.grid.add_column(name="assemblies", size=60)
        self.grid.add_column(name="instances", size=45)
        self.grid.add_column(name="dumparea")
        self.grid.add_row(name="top", size=3)
        self.grid.add_row(name="middle", min_size=40)
        self.grid.add_row(name="bottom", size=7)

        self.grid.set_align("stretch", "center")

        self.grid.add_areas(
            title="info-start|info-end,top-start|top-end",
            dirtree="info-start|info-end,middle-start|middle-end",
            summary="info-start|info-end,bottom-start|bottom-end",
            filter_="assemblies-start|assemblies-end,top-start|top-end",
            list_="assemblies-start|assemblies-end,top-end|bottom-end",
            instance_title="instances-start|instances-end,top-start|top-end",
            instancelist="instances-start|instances-end,top-end|bottom-end",
            dump_title="dumparea-start|dumparea-end,top-start|top-end",
            dumparea="dumparea-start|dumparea-end,top-end|bottom-end",
        )

        # Create the info column widgets
        self.file_explorer = ScrollView(
            DoubleClickDirectoryTree(str(Path.cwd()), "Directory"),
            auto_width=True,
            name="fileexplorerview",
        )
        self.summary = Static("")

        # Create the assembly column widgets
        self.assembly_filter = TextInput(placeholder="Search assemblies")
        self.assembly_filter.on_change_handler_name = "handle_filter_on_change"
        self.assembly_list = AssemblyTree("", data=[], name="AssemblyList")
        self.assembly_list_view = ScrollView(
            self.assembly_list, auto_width=True, name="assemblylistview"
        )
        self.assembly_list_view.vscroll = TurdshovelScrollBar()
        self.assembly_list_view.hscroll = TurdshovelScrollBar(vertical=False)

        # Create the instance column widgets
        self.assembly_instances_list = AssemblyInstanceTree(
            "", data=[], name="InstanceList"
        )
        self.assembly_instances_view = ScrollView(
            self.assembly_instances_list, auto_width=True, name="instancelistview"
        )
        self.assembly_instances_view.vscroll = TurdshovelScrollBar()
        self.assembly_instances_view.hscroll = TurdshovelScrollBar(vertical=False)

        # Create the text area
        self.dumpview = ScrollView(auto_width=True, name="dumpview", fluid=False)
        self.dumpview.vscroll = TurdshovelScrollBar()
        self.dumpview.hscroll = TurdshovelScrollBar(vertical=False)

        # Everything in its place
        self.grid.place(
            title=Title("Turdshovel 1.0.0a"),
            dirtree=self.file_explorer,
            summary=self.summary,
            filter_=self.assembly_filter,
            list_=self.assembly_list_view,
            instance_title=Title("Assembly Instances"),
            instancelist=self.assembly_instances_view,
            dump_title=Title("Output"),
            dumparea=self.dumpview,
        )

    async def _update_assembly_list(self, available_types: str):
        """Update the list of available assemblies"""
        self.assembly_list = AssemblyTree(
            self._dump_summary.dumpfile_path.name, data=[], name=self.assembly_list.name
        )
        [
            await self.assembly_list.add(self.assembly_list.root.id, t, t)
            for t in available_types
        ]
        await self.assembly_list.root.expand()
        await self.assembly_list_view.update(self.assembly_list)
        self.assembly_list_view.refresh(layout=True)

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked."""

        if summary := DumpFile.from_dumpfile(Path(message.path)):
            self._dump_summary = summary
            await self.summary.update(summary)
            await self._update_assembly_list(summary.available_types)

    async def handle_filter_on_change(self, message: Message):
        if self._dump_summary:
            filter_value = message.sender.value.lower()
            filtered_types = [
                type_
                for type_ in self._dump_summary.available_types
                if filter_value in type_.lower()
            ]
            await self._update_assembly_list(filtered_types)


@cli_app.command()
def run():
    Turdshovel.run(log="textual.log")


if __name__ == "__main__":
    cli_app()
