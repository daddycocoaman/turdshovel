import shutil
import subprocess
import shlex
from pathlib import Path
import os

TURDSHOVEL_DLLS = Path(__file__).parents[1] / "turdshovel/_dlls"
IRONSTUBS_DIR = Path(__file__).parents[1] / "ironpython-stubs"
TURDSTUBS_DIR = Path(__file__).parents[1] / "turdshovel/_stubs"

os.chdir(IRONSTUBS_DIR)

gen = subprocess.Popen(
    shlex.split(
        f"ipy.exe -m ironstubs make --all --path='{TURDSHOVEL_DLLS.absolute()}' --output turdshovel_stubs.min"
    ),
    shell=True,
)
gen.wait()

shutil.copytree(
    str(IRONSTUBS_DIR / "release/turdshovel_stubs.min"),
    str(TURDSTUBS_DIR),
    dirs_exist_ok=True,
)

shutil.rmtree(IRONSTUBS_DIR / "release/turdshovel_stubs.min", ignore_errors=True)
