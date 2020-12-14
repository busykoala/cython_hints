from cython_hints.demo_cython import cython_fib
from cython_hints.demo_cython import cython_fib_typed
from cython_hints.demo_cython import use_c_function
from cython_hints.demo_cython import use_cpp_function
from cython_hints.demo_cython import fib_cdef
from cython_hints.demo_cython import fib_cpdef
from cython_hints.demo_cpp import ext_cpp_fib
from cython_hints.demo_c import ext_c_fib
import time


def python_fib(n):
    if n <= 1:
        return n
    else:
        return python_fib(n - 1) + python_fib(n - 2)


def benchmark():
    tic = time.perf_counter()
    python_fib(40)
    toc = time.perf_counter()
    python_time = toc - tic
    print(f'Time Python: {python_time:0.4f}')

    tic = time.perf_counter()
    cython_fib(40)
    toc = time.perf_counter()
    cython_time = toc - tic
    print(f'Time Cython: {cython_time:0.4f}')

    tic = time.perf_counter()
    cython_fib_typed(40)
    toc = time.perf_counter()
    cython_typed_time = toc - tic
    print(f'Time Cython Typed: {cython_typed_time:0.4f}')

    tic = time.perf_counter()
    fib_cpdef(40)
    toc = time.perf_counter()
    fib_cpdef_time = toc - tic
    print(f'Time Cython hyprid Cpp: {fib_cpdef_time:0.4f}')

    tic = time.perf_counter()
    fib_cdef(40)
    toc = time.perf_counter()
    fib_cdef_time = toc - tic
    print(f'Time Cython hybrid C: {fib_cdef_time:0.4f}')

    tic = time.perf_counter()
    ext_cpp_fib(40)
    toc = time.perf_counter()
    ext_cpp_fib_time = toc - tic
    print(f'Time Cython lib Cpp: {ext_cpp_fib_time:0.4f}')

    tic = time.perf_counter()
    ext_c_fib(40)
    toc = time.perf_counter()
    ext_c_fib_time = toc - tic
    print(f'Time Cython lib C: {ext_c_fib_time:0.4f}')


def main():
    print(f'Example use of C std function - Result: {use_c_function(1)}')
    print(f'Example use of Cpp std function - Result: {use_cpp_function(b"hello world")}')

    print('\n###################\n# Start Benchmark #\n###################\n')
    benchmark()
