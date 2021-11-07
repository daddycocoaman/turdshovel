from pathlib import Path

from Microsoft.Diagnostics.Runtime import DataTarget
from nubia import argument, command, context
from rich import inspect
from rich.console import Console
from rich.table import Table
from sortedcontainers import SortedSet
from ..context import TurdshovelContext


@command
@argument("dumpfile", type=Path, positional=True, description="Path to .NET dump")
def load(dumpfile: Path) -> None:
    """Loads a dump for a session"""

    ctx: TurdshovelContext = context.get_context()
    console: Console = ctx.console

    ctx.target = DataTarget.LoadDump(str(dumpfile))
    # inspect(ctx.target, all=True)
    summary = Table(
        *["Clr Version", "Properties"],
        title=str(dumpfile.absolute()),
        border_style="bold #8B4513",
        title_style="bold cyan",
    )
    for version in ctx.target.ClrVersions:
        dacInfo = version.DacInfo
        info = f"Filesize: {int(dacInfo.IndexFileSize)}\n"
        info += f"Timestamp: {int(dacInfo.IndexTimeStamp)}\n"
        info += f"Dac File: {dacInfo.PlatformSpecificFileName}\n"
        info += f"Local Dac Found: {bool(dacInfo.LocalDacPath)}"

        summary.add_row(str(version.Version), info)

    load_success = False
    try:
        ctx.runtime = ctx.target.ClrVersions[0].CreateRuntime()
        summary.caption = f"[green bold] :white_heavy_check_mark: Successfully created {ctx.target.ClrVersions[0].Version} runtime object!\n[/]"
        ctx.target_friendly_name = dumpfile.name
        load_success = True
    except:
        summary.caption = f"[red bold] :no-entry: Could not create {ctx.target.ClrVersions[0].Version} runtime object!\n[/]"
        console.print_exception()

    console.print(summary, new_line_start=True)

    # If we successfully load, do some analysis and reload commands
    if load_success:
        with console.status(
            "[bold green]Analyzing dump...", spinner="toggle10"
        ) as status:

            ### Getting objects to prepopulate
            ctx.available_obj_types = SortedSet()
            if ctx.runtime.Heap.CanWalkHeap:
                for segment in ctx.runtime.Heap.Segments:
                    for obj in segment.EnumerateObjects():
                        if obj.IsValid and not obj.IsFree:
                            ctx.available_obj_types.add(str(obj.Type))
                console.print(
                    f":white_heavy_check_mark: Found {len(ctx.available_obj_types)} unique .NET object types"
                )

            ctx.reload_commands()
            console.print(":white_heavy_check_mark: Reloaded commands\n")
