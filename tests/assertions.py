import os
import subprocess
import sys
from tempfile import NamedTemporaryFile

from sure import assertion


def _diff(this, that):
    this_f = NamedTemporaryFile()
    this_f.write(this)
    this_f.flush()
    that_f = NamedTemporaryFile()
    that_f.write(that)
    that_f.flush()
    cmd = f"diff -u {this_f.name} {that_f.name} || true"
    return subprocess.check_output(cmd, shell=True)


@assertion
def match_snapshot(self, snapshot, transformer=None):
    full_path = f"tests/snapshots/{snapshot}"
    assert os.path.isfile(full_path), f"Couldn't find snapshot '{snapshot}'"

    with open(full_path) as f:
        that = f.read()

    # apply optional transformer
    this = self.obj

    if transformer:
        this = transformer(this)
        that = transformer(that)

    if self.negative:
        if this == that:
            sys.stderr.write(f"Content:\n{this}\n")
            raise AssertionError(
                f"Content should differ from {snapshot}, but is the same thing"
            )

    else:
        if this != that:
            sys.stderr.write(f"Diff:\n{_diff(this, that)}\n")
            raise AssertionError(
                f"Content differ from {snapshot}, see stderr output for a diff."
            )

    return True
