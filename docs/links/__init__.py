# from os.path import dirname, basename, isfile

# import glob
# modules = glob.glob(dirname(__file__)+"/*.py")

# __all__ = [ basename(f)[:-3] for f in modules if isfile(f)]

import sphinx.ext.extlinks as links

from links.link import *
from links import *