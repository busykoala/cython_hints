from libc.math cimport sin as csin
from libcpp.string cimport string as cpp_string


def common_function(a, b):
    """This is pretty slow because not type safe.
    """
    return a + b


def type_safe_function(int a, int b) -> int:
    """This can accelerate a little.
    """
    return a + b


def use_c_function(double a) -> double:
    """This function demonstrates the use of a C standard library function.
    """
    return csin(a)


def use_cpp_function():
    """This function demonstrates the use of a C++ standard library function.
    """
    py_bytes_object = b'hello world'
    cdef cpp_string example_string = py_bytes_object
    return example_string


cpdef int fib_cpdef(int n):
    """This function will be created in python and in C

    If it's called from cython the C version is used otherwise
    the python one.
    """
    if n < 2:
        return n
    return fib_cpdef(n-2) + fib_cpdef(n-1)


def fib_cdef(int n) -> int:
    """This function is usable in python code but calles fib_in_c.
    """
    return fib_in_c(n)


cdef int fib_in_c(int n):
    """This is only accessable from cython. To use it outside we need a helper.
    """
    if n < 2:
        return n
    return fib_in_c(n-2) + fib_in_c(n-1)
