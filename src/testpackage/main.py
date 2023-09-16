"""module run.py docstring"""

from . import _mydemo

def hello():
    """test message""" 
    print('Hello world, this is "run.py"')

def mydemo():
    print("_mydemo.print_hello()")
    output  = _mydemo.print_hello()
    print("output:", output)
    print(f"__doc__ = {_mydemo.__doc__}")
    print(f"__file__ = {_mydemo.__file__}")
    print(f"__name__ = {_mydemo.__name__}")
    print(f"__package__ = {_mydemo.__package__}")
