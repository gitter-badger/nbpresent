from subprocess import Popen
import sys

from ._env import (
    DIST,
    SRC,
    join,
    node_bin,
)


def main(**opts):
    args = [
        node_bin("lessc"),
        "--autoprefix",
        "--clean-css",
        join(SRC, "less", "index.less"),
        join(DIST, "nbpresent.min.css")
    ] + opts.get("less", [])
    return Popen(args).wait()


if __name__ == "__main__":
    sys.exit(main())
