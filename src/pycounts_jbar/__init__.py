# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_jbar")

from pycounts_jbar.pycounts_jbar import count_words
from pycounts_jbar.plotting import plot_words