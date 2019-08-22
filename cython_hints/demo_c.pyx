cdef extern from "c_src/cfib.h":
    int cfib(int n)


def ext_c_fib(int n) -> int:
    """Returns the nth Fibonacci number from C."""
    return cfib(n)
