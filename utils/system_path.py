import sys
import os
def path():
    # Add the project root directory to the system path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    sys.path.append(project_dir)