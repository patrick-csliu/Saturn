"""module run.py docstring"""

import math
from . import mydemo

def cos10():
    """cos(10)""" 
    return math.cos(10)

def hello():
    """test message""" 
    print('Hello world, this is "run.py"')

output  = mydemo.print_hello()
print(output)
