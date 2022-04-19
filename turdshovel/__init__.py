import logging
import sys
from pathlib import Path

from pythonnet import set_default_runtime
from rich import pretty, traceback
from rich.logging import RichHandler

# Add .NET assemblies to sys.path
assembly_path = Path(__file__).parent / "_dlls"
sys.path.append(str(assembly_path))

# Import clr and add assembly references
set_default_runtime()
import clr
import System

[clr.AddReference(str(assembly)) for assembly in assembly_path.glob("*.dll")]

# Handle redirects or else might get dependency errors
def assembly_resolve(app_domain, resolve_event_args):
    name = resolve_event_args.Name.split(",")[0]
    try:
        return next(x for x in app_domain.GetAssemblies() if x.GetName().Name == name)
    except StopIteration:
        pass


System.AppDomain.CurrentDomain.AssemblyResolve += assembly_resolve

# Add Rich!
pretty.install()
traceback.install(show_locals=True)


FORMAT = "%(message)s"
logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
