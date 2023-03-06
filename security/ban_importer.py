# ban_importer.py

import sys

import numpy
import matplotlib
from matplotlib import *

BANNED_MODULES = {'os'}

class BanFinder:
    @classmethod
    def find_spec(cls, name, path, target=None):
        if path is not None:
            return
        if name in BANNED_MODULES:
            raise ModuleNotFoundError(f"{name!r} is banned")

sys.meta_path.insert(0, BanFinder)

del sys.modules['os']