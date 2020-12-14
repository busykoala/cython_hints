from cython_hints.demo_cython import cython_fib
from cython_hints.demo_cython import cython_fib_typed
from cython_hints.demo_cython import use_c_function
from cython_hints.demo_cython import use_cpp_function
from cython_hints.demo_cython import fib_cdef
from cython_hints.demo_cython import fib_cpdef
from cython_hints.demo_cpp import ext_cpp_fib
from cython_hints.demo_c import ext_c_fib


def test_cython_fib():
    assert cython_fib(30) == 832040


def test_cython_fib_typed():
    assert cython_fib_typed(30) == 832040


def test_use_c_function():
    assert use_c_function(1) == 0.8414709848078965


def test_use_cpp_function():
    assert use_cpp_function(b'hello world') == [b'hello', b'world']


def test_fib_cdef():
    assert fib_cdef(30) == 832040


def test_fib_cpdef():
    assert fib_cpdef(30) == 832040


def test_ext_cpp_fib():
    assert ext_cpp_fib(30) == 832040


def test_ext_c_fib():
    assert ext_c_fib(30) == 832040
