import os
from sure import assertion
from sure.core import DeepComparison, DeepExplanation, safe_repr


@assertion
def match_snapshot(self, snapshot):
    full_path = "tests/snapshots/{}".format(snapshot)
    assert os.path.isfile(full_path), \
        "Couldn't find snapshot '{}'".format(snapshot)

    with open(full_path) as f:
        what = f.read()

    # below code adapted from "equal()" matcher
    # see: https://github.com/gabrielfalcao/sure/blob/master/sure/__init__.py
    try:
        comparison = DeepComparison(self.obj, what).compare()
        error = False
    except AssertionError as e:
        error = e
        comparison = None

    if isinstance(comparison, DeepExplanation):
        error = comparison.get_assertion(self.obj, what)

    if self.negative:
        if error:
            return True

        msg = '%s should differ from %s, but is the same thing'
        raise AssertionError(msg % (safe_repr(self.obj), safe_repr(what)))

    else:
        if not error:
            return True
        raise error
