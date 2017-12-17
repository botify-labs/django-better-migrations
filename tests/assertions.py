import os
import subprocess
from sure import assertion
import sys
from tempfile import NamedTemporaryFile


def _diff(this, that):
    this_f = NamedTemporaryFile()
    this_f.write(this)
    this_f.flush()
    that_f = NamedTemporaryFile()
    that_f.write(that)
    that_f.flush()
    cmd = "diff -u {} {} || true".format(this_f.name, that_f.name)
    return subprocess.check_output(cmd, shell=True)


@assertion
def match_snapshot(self, snapshot, transformer=None):
    full_path = "tests/snapshots/{}".format(snapshot)
    assert os.path.isfile(full_path), \
        "Couldn't find snapshot '{}'".format(snapshot)

    with open(full_path) as f:
        that = f.read()

    # apply optional transformer
    this = self.obj

    if transformer:
        this = transformer(this)
        that = transformer(that)

    if self.negative:
        if this == that:
            sys.stderr.write("Content:\n{}\n".format(this))
            raise AssertionError(
                "Content should differ from {}, but is the same thing".format(snapshot))

    else:
        if this != that:
            sys.stderr.write("Diff:\n{}\n".format(_diff(this, that)))
            raise AssertionError(
                "Content differ from {}, see stderr output for a diff.".format(snapshot))

    return True
