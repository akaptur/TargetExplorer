import os, sys

this_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, this_dir)
from config import targetexplorer_install_dir
sys.path.insert(0, targetexplorer_install_dir)

from app import app as application