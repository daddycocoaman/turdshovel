import shutil
from pathlib import Path

NUGET_DIR = Path(__file__).parents[1] / ".nuget"
TURDSHOVEL_DLLS = Path(__file__).parents[1] / "turdshovel/_dlls"

for file in NUGET_DIR.glob("*/lib/netstandard2.0/*"):
    # Need to unblock files since downloaded from internet
    Path(str(file) + ":Zone.Identifier").unlink(missing_ok=True)
    shutil.copy(file, TURDSHOVEL_DLLS)
