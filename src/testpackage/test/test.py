"""test package"""

from testpackage import run
from testpackage import mydemo

print(run.cos10())
run.hello()

value = mydemo.print_hello()
print(f"output from mydemo.print_hello(): {value}")
