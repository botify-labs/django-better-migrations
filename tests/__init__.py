# Disable sure's patched "dir" builtin, since it breaks on OSX
# with an error similar to: https://github.com/benjaminp/six/issues/54
# (having sure AND six AND tox trying to monkey-patch things might be too much)
from sure import builtins, old_dir

from . import assertions

builtins.dir = old_dir

__all__ = ["assertions"]
