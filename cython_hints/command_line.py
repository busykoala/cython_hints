from cython_hints.demo_cython import common_function
from cython_hints.demo_cython import type_safe_function
from cython_hints.demo_cython import use_c_function
from cython_hints.demo_cython import use_cpp_function
from cython_hints.demo_cython import fib_cdef
from cython_hints.demo_cython import fib_cpdef
from cython_hints.demo_cpp import ext_cpp_fib
from cython_hints.demo_c import ext_c_fib


def main():
    print(common_function(1, 3))
    print(type_safe_function(1, 3))

    print(use_c_function(1))
    print(use_cpp_function())

    print(fib_cdef(30))
    print(fib_cpdef(30))

    print(ext_cpp_fib(30))
    print(ext_c_fib(30))
