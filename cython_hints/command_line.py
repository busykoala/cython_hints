from demo_module import common_function
from demo_module import type_safe_function
from demo_module import use_c_function
from demo_module import use_cpp_function
from demo_module import fib_cdef
from demo_module import fib_cpdef


def main():
    print(common_function(1, 3))
    print(type_safe_function(1, 3))
    print(use_c_function(1))
    print(use_cpp_function())
    print(fib_cdef(30))
    print(fib_cpdef(30))
