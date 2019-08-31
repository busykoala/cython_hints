# Cython Hints

This package demonstrates some usefull cases how to use cython.

## Where to find what

In `demo_cython.pyx` there are examples for:

- common function (cython "precompiled")
- type safe function (cython "precompiled")
- use c function from std lib
- use cpp function from std lib
- both python an c function (great for recursion)
- a "c compiled" function given a python wrapper.

In `demo_c.pyx` there is an example for external c code used
within python.

In `demo_cpp.pyx` there is an example for external cpp code
used within python. 

## Cool resources

Quite a bit explained how stuff works in cython this resource is also
very much readable: [Okigiveup](http://okigiveup.net/an-introduction-to-cython/)

## Installation

```
git clone git@github.com:busykoala/cython_hints.git
cd cython_hints
python3 -m venv .
source ./bin/activate
pip install -e .
```

## Run

```
show_magic
```

## Testing

```
source ./bin/activate
pip install -e ".[test]"
python -m pytest
```
