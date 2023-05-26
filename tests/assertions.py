import difflib
import os
import sys

from sure import assertion


def _diff(this: str, that: str):
    return "".join(
        difflib.unified_diff(
            this.splitlines(keepends=True), that.splitlines(keepends=True)
        )
    )


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
