from nubia import command, context


@command
def reload() -> None:
    """Reload commands"""

    ctx = context.get_context()
    ctx.reload_commands()

    ctx.console.print("[green bold]:white_heavy_check_mark: Reloaded commands!")
