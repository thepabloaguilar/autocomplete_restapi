import os

from .tree import TernaryTree

def get_tree():
    tree = TernaryTree()

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(curr_dir, 'patients.csv')
    
    with open(path) as _file:
        for line in _file:
            tree.insert(line)
    
    return tree