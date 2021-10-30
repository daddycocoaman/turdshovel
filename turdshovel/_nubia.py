from rich import box
from rich.table import Table
from rich import print
from nubia import context
from nubia.internal.commands.builtin import Exit
from nubia.internal.commands.help import HelpCommand
from nubia.internal.exceptions import UnknownCommand, CommandError


class _Exit(Exit):
    cmd = ["exit"]

    def __init__(self):
        super(Exit, self).__init__()

    def run_interactive(self, cmd, args, raw):
        ctx = context.get_context()
        ctx.console.set_alt_screen(False)
        raise EOFError()


class _Help(HelpCommand):
    cmds = {"help": HelpCommand.HELP}

    def __init__(self):
        super(HelpCommand, self).__init__()

    # Overwrite function to use Rich instead of PrettyTable. Also remove built-in table
    def run_interactive(self, _0, args, _2):
        if args:
            args = args.split()
            try:
                cmd_instance = self.registry.find_command(args[0])
                if not cmd_instance:
                    raise UnknownCommand("Command `{}` is " "unknown".format(args[0]))
                else:
                    help_msg = cmd_instance.get_help(args[0].lower(), *args)
                print(help_msg)
            except CommandError as e:
                print(str(e), "red")
                return 1
        else:
            table = Table(style="#52311A", header_style="bold #8E562E", box=box.ROUNDED)
            table.add_column("Command", style="yellow")
            table.add_column("Description", style="green")

            commands = {
                cmd_name: cmd
                for cmd in self.registry.get_all_commands()
                for cmd_name in cmd.get_command_names()
            }

            for cmd_name in sorted(commands):
                cmd = commands[cmd_name]
                cmd_help = cmd.get_help(cmd_name)
                table.add_row(cmd_name, cmd_help)

            print(table)
            return 0
