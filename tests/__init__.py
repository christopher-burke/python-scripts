"""Unittests for library.


Run using `python -m unittest` in the top level directory folder.
"""

import os
import sys

add_path = os.path.dirname(os.path.dirname((os.path.realpath(__file__))))

# Ensure that the script lib is on path for imports.
sys.path.insert(0, add_path)
