"""test package"""

from testpackage import run
from testpackage import _mydemo

run.hello()

value = _mydemo.print_hello()
print(f"output from mydemo.print_hello(): {value}")
