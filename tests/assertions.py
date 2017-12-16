import os
from sure import assertion
from sure.core import DeepComparison, DeepExplanation, safe_repr


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

    # change string to lines so diffs look better
    this = this.splitlines()
    that = that.splitlines()

    # below code adapted from "equal()" matcher
    # see: https://github.com/gabrielfalcao/sure/blob/master/sure/__init__.py
    try:
        comparison = DeepComparison(this, that).compare()
        error = False
    except AssertionError as e:
        error = e
        comparison = None

    if isinstance(comparison, DeepExplanation):
        error = comparison.get_assertion(this, that)

    if self.negative:
        if error:
            return True

        msg = '%s should differ from %s, but is the same thing'
        raise AssertionError(msg % (safe_repr(this), safe_repr(that)))

    else:
        if not error:
            return True
        raise error
