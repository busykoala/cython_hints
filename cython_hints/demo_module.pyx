from libc.math cimport sin as csin


def common_function(a, b):
    """This is still pretty slow because not type safe.
    """
    return a + b


def type_safe_function(a: int, b: int) -> int:
    """This can accelerate quite a bit and is still written in python.
    """
    return a + b


def use_c_function(a: double) -> double:
    """This function demonstrates the use of a C standard library function.
    """
    return csin(a)


def use_cpp_function():
    """This function demonstrates the use of a CPP standard library function.
    """
    # to be done
    pass


def make_use_of_cdef_and_at_cython_cfunc():
    """Define with cdef or set a decorator with @cython.cfunc
    """
    # to be done
    pass
