import time
from typing import List

import orjson
import numpy as np
import System
from nubia import argument, command, context
from rich import inspect
from rich.console import Console
from rich.table import Table

from ..context import TurdshovelContext
from ..core.parsing import parse_obj


@command
class Dump:
    """Dump commands"""

    def __init__(self) -> None:
        self.ctx: TurdshovelContext = context.get_context()
        self.runtime = self.ctx.runtime
        self.console: Console = self.ctx.console

    @command
    @argument(
        "filter_", type=List[str], name="filter", description="Filter objects by string"
    )
    def heap(self, filter_: List[str] = ["."]) -> None:
        """Dumps the objects on the heap"""

        if not self.ctx.runtime:
            self.console.print("[bold red] No runtime loaded! Load a dump first!")
            return

        object_table = Table(border_style="#8B4513")
        object_table.add_column("Address", style="cyan")
        object_table.add_column("Size", style="green")
        object_table.add_column("Object", style="yellow", overflow="fold")

        for segment in self.runtime.Heap.Segments:
            for obj in segment.EnumerateObjects():
                if obj.IsValid and not obj.IsFree:
                    if any(f.lower() in obj.ToString().lower() for f in filter_):
                        object_table.add_row(
                            hex(obj.Address),
                            str(obj.Size),
                            obj.ToString().rsplit(maxsplit=1)[0],
                        )
        self.console.print(object_table, highlight=True)

    @command
    @argument(
        "address",
        type=str,
        positional=True,
        description="Address of object to dump. Hex format (0x12345678)",
    )
    @argument("save", type=bool, description="Save output to disk")
    def obj(self, address: str, save: bool = False) -> None:
        """Dumps an object on the heap by address"""

        # TODO: Turn this into a decorator for reuse
        if not self.ctx.runtime:
            self.console.print("[bold red] No runtime loaded! Load a dump first!")
            return

        address = int(address, 16)
        obj = self.runtime.Heap.GetObject(address)

        # We only care about valid objects and non-Free objects
        if obj.IsValid and not obj.IsFree:
            if obj.IsArray:
                output = []
                obj_list = obj.AsArray()
                for idx in range(0, obj_list.Length):
                    item = obj_list.GetObjectValue(idx)
                    if not item.IsNull:
                        output.append(parse_obj(self.runtime, item, self.console))
            else:
                output = parse_obj(self.runtime, obj, self.console)

            output = orjson.dumps(output, default=lambda x: repr(x))
            if save:
                filename = f"{self.ctx.target_friendly_name}_{hex(address)}_{time.strftime('%Y%m%d-%H%M%S')}.json"
                with open(filename, "wb") as save_file:
                    save_file.write(output)
                self.console.print(f"[green bold]Output saved to {filename}")
            else:
                try:
                    self.console.print_json(output.decode())
                except:
                    self.console.print(output)

    @command
    @argument(
        "address",
        type=str,
        positional=True,
        description="Address in memory to dump. Hex format (0x12345678)",
    )
    @argument(
        "length", type=int, positional=True, description="Length of bytes to dump"
    )
    def mem(self, address: str, length: int) -> None:
        """Dumps the memory in bytes at location and for length specified"""

        output_span = System.Span[System.Byte](bytes(length))
        self.runtime.DataTarget.DataReader.Read(
            np.uint64(int(address, 16)), output_span
        )

        output_str = "".join([f"{i:02x}" for i in output_span.ToArray()])
        self.console.print(f"Hex: ", output_str)
        self.console.print(f"Bytes: ", bytes.fromhex(output_str))
        try:
            self.console.print(
                f"ASCII: ", bytes.fromhex(output_str).decode(), highlight=False
            )
        except:
            pass

    @command
    @argument(
        "types",
        type=List[str],
        description="Dump objects by type",
        choices=context.get_context().available_obj_types,
    )
    @argument("save", type=bool, description="Save output to disk")
    def type_(self, types: List[str], save: bool = False) -> None:
        """Dumps the objects on the heap"""

        if not self.ctx.runtime:
            self.console.print("[bold red] No runtime loaded! Load a dump first!")
            return

        for segment in self.runtime.Heap.Segments:
            for obj in segment.EnumerateObjects():
                if obj.IsValid and not obj.IsFree:
                    if any(_ == str(obj.Type) for _ in types):
                        self.obj(hex(obj.Address), save)
