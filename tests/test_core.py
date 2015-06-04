"""
Unittests for `gpsdio_xz.core`.
"""


import tempfile
import gpsdio
import datetime
import os.path
import random
import contextlib
import glob

def randdate():
    return datetime.datetime(
        2014, 1+int(12*random.random()),
        1+int(28*random.random()),
        int(24*random.random()),
        int(60*random.random()),
        int(60*random.random())
        )


@contextlib.contextmanager
def unittestfiles():
    try:
        yield
    finally:
        for name in glob.glob("unittest.out.*"):
            os.unlink(name)

def test_sort():
    with unittestfiles():
        with gpsdio.open('unittest.out.msg.xz', "w") as f:
            f.writerows([
                    {"mmsi": "123", "name": "Rainbow warrior", "speed": 1.0},
                    {"name": "France", "speed": 1.1},
                    {"mmsi": "456", "name": "Rainbow warrior II", "speed": 2.0}
                    ])
        with gpsdio.open('unittest.out.msg.xz') as f:
            rows = list(f)

        assert len(rows) == 3
        assert rows[0]["name"] == "Rainbow warrior"
