import argparse
import logging

from nubia import PluginInterface
from rich import print
from rich.logging import RichHandler

from .context import TurdshovelContext


class TurdshovelPlugin(PluginInterface):
    """
    The TurdshovelPlugin sets the configuration for the CLI
    """

    def create_context(self):
        return TurdshovelContext()

    def validate_args(self, args):
        pass

    def get_opts_parser(self, add_help=True):
        opts_parser = argparse.ArgumentParser(
            description="Turdshovel CLI for dumping secrets from .NET dumps",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=add_help,
        )
        opts_parser.add_argument(
            "--verbose", "-v", action="store_true", help="Verbose output"
        )
        return opts_parser

    def setup_logging(self, root_logger, args):
        logging.basicConfig(
            level=logging.DEBUG if args.verbose else logging.INFO,
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(rich_tracebacks=True, markup=True)],
        )
        return logging.getLogger("rich")
