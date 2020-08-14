"""Script to call executables in `tox` envs.

The script takes two mandatory arguments:
1. the executable to call like e.g. `pylint`
2. a string with comma separated `tox` envs to check for the executable

All other arguments after are passed to the tool on call.

The script considers OS and calls the tool accordingly.
"""
import subprocess  # nosec
import sys

from pathlib import Path


def main():
    """Call given `tool` from given `tox` env."""
    tool = sys.argv[1]

    if sys.platform == "win32":
        exe = Path("Scripts/" + tool + ".exe")
    else:
        exe = Path("bin/" + tool)

    tox = Path(".tox")
    envs = sys.argv[2].split(",")

    cmd = None
    for env in envs:
        path = Path(tox / env / exe)
        if path.is_file():
            cmd = (str(path), *sys.argv[3:])

    if cmd is None:
        print(
            "No '{}' executable found. Make sure one of the "
            "following `tox` envs is accessible: {}".format(tool, envs)
        )
        return 1

    return subprocess.call(cmd)  # nosec


if __name__ == "__main__":
    sys.exit(main())
