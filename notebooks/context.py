import os
import sys

"""
This file basically makes sure that we can import robot_judge and its subpackages correctly from notebooks
which are stored in the notebooks directory as

    from context import robot_judge
    
From this point on we can import anything from ml_project as we wish.
"""

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import robot_judge