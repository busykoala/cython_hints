cdef extern from "cpp_src/cppfib.h":
    int cppfib(int n)


def ext_cpp_fib(int n) -> int:
    """Returns the nth Fibonacci number from C++."""
    return cppfib(n)
