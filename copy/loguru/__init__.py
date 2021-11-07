"""
The Loguru library provides a pre-instanced logger to facilitate dealing with logging in Python.

Just ``from loguru import logger``.
"""
import atexit as _atexit
import sys as _sys

from . import _defaults
from ._logger import Core as _Core
from ._logger import Logger as _Logger

__version__ = "0.5.3"

__all__ = ["logger"]

logger = _Logger(_Core(), None, 0, False, False, False, False, True, None, {})

if _defaults.LOGURU_AUTOINIT and _sys.stderr:
    logger.add(_sys.stderr)

_atexit.register(logger.remove)
