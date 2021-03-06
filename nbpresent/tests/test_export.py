from glob import glob
import os
import socket
import subprocess
import tempfile
import sys
import shutil

from ..export import export


# utility function
def join(*bits): return os.path.abspath(os.path.join(*bits))


here = os.path.dirname(__file__)

http_module = None

try:
    import http.server as httpd
    http_module = "http.server"
except ImportError:
    import SimpleHTTPServer as httpd
    http_module = "SimpleHTTPServer"

print("nbpresent export test using", httpd)


def unused_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    addr, port = sock.getsockname()
    sock.close()
    return port


def test_export():
    tmpdir = tempfile.mkdtemp()
    env = dict(os.environ)
    env.update(
        NBPRESENT_TEST_HTTP_PORT=str(unused_port())
    )

    httpd = subprocess.Popen([
            sys.executable, "-m", http_module,
            env["NBPRESENT_TEST_HTTP_PORT"],
            "--bind=127.0.0.1"
        ],
        cwd=tmpdir)

    try:
        export(
            join(here, "notebooks", "Basics.ipynb"),
            join(tmpdir, "Basics.html"),
            "html")

        assert 0 == subprocess.Popen([
                "casperjs", "test",
                "--includes={}".format(
                    ",".join(glob(join(here, 'js', '_*.js')))),
            ] + glob(join(here, 'js', 'test_export_*.js')),
            env=env).wait()
    finally:
        httpd.kill()
        shutil.rmtree(tmpdir)


if __name__ == '__main__':
    test_export()
