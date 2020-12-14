from libc.math cimport sin as csin
from libcpp.string cimport string as cpp_string
from libcpp.vector cimport vector as cpp_vector
from typing import ByteString
from typing import List


def cython_fib(n):
    """This function is precompiled but still pretty slow.
    """
    if n <= 1:
        return n
    else:
        return cython_fib(n - 1) + cython_fib(n - 2)


def cython_fib_typed(n: int) -> int:
    """This function is precompiled and because it's typed it should be a bit faster.
    """
    if n <= 1:
        return n
    else:
        return cython_fib(n - 1) + cython_fib(n - 2)


def use_c_function(double a) -> double:
    """This function demonstrates the use of a C standard library function.
    """
    return csin(a)


def use_cpp_function(py_bytes_obj: ByteString) -> List[ByteString]:
    """This function demonstrates the use of a C++ standard library function.
    """
    cdef cpp_vector[cpp_string] example_vector = py_bytes_obj.split()
    return example_vector


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
