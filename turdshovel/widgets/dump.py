from enum import Enum
from pathlib import Path
from typing import List

from Microsoft.Diagnostics.Runtime import Architecture, ClrRuntime, DataTarget
from rich import box
from rich.table import Table
from sortedcontainers import SortedSet
from textual.widget import Widget


class DumpMessage(str, Enum):
    SUCCESS = "[green]Success[/]"
    HEAP_WALK_FAIL = "[red]Can't walk the heap![/]"


class DumpFile(Widget):
    def __init__(
        self,
        runtime: ClrRuntime,
        dumpfile_path: Path,
        clr_version: str,
        filesize: int,
        message: str,
        target_arch: Architecture,
        available_types: List[str],
        name: str = None,
    ) -> None:
        super().__init__(name)
        self.dumpfile_path = dumpfile_path
        self.clr_version = clr_version
        self.filesize = filesize
        self.available_types = available_types
        self.target_arch = target_arch
        self.num_types = len(available_types)
        self.message = message
        self.app.runtime = runtime

    @classmethod
    def from_dumpfile(cls, dumpfile: Path) -> "DumpFile":
        try:
            target = DataTarget.LoadDump(str(dumpfile))
            runtime = target.ClrVersions[0].CreateRuntime()
            if not runtime.Heap.CanWalkHeap:
                message = DumpMessage.HEAP_WALK_FAIL
            else:
                available_obj_types = SortedSet()
                for segment in runtime.Heap.Segments:
                    for obj in segment.EnumerateObjects():
                        if obj.IsValid and not obj.IsFree:
                            available_obj_types.add(str(obj.Type))
                message = DumpMessage.SUCCESS

            clr_ver = target.ClrVersions[0]
            return cls(
                runtime=runtime,
                dumpfile_path=dumpfile,
                clr_version=str(clr_ver.DacInfo.Version),
                filesize=int(clr_ver.DacInfo.IndexFileSize),
                target_arch=str(clr_ver.DacInfo.TargetArchitecture),
                message=message,
                available_types=available_obj_types,
                name="DumpSummary",
            )
        except Exception as e:
            return

    def render(self) -> Table:
        table = Table(
            "Name",
            "Value",
            border_style="#0085a8",
            box=box.ROUNDED,
            show_header=False,
            highlight=True,
            expand=True,
        )
        table.add_row("CLR", self.clr_version)
        table.add_row("Size", str(self.filesize))
        table.add_row("NumTypes", str(self.num_types))
        table.add_row("Arch", self.target_arch)
        table.add_row("Msg", self.message)
        return table
