from setuptools.extension import Extension
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'cython_hints'
VERSION = '0.0.1'
AUTHOR = 'Busykoala'
EMAIL = 'info@busykoala.ch'
DESCRIPTION = 'Demonstrate Cython'
URL = 'https://git.sr.ht/~busykoala/cython_hints'
REQUIRED = []

EXTENSIONS = [
    Extension(
        'cython_hints.demo_cython',
        sources=['cython_hints/demo_cython.pyx'],
        language='c++'
    ),
    Extension(
        'cython_hints.demo_cpp',
        sources=['cython_hints/demo_cpp.pyx', 'cython_hints/cpp_src/cppfib.cpp'],
        language='c++'
    ),
    Extension(
        'cython_hints.demo_c',
        sources=['cython_hints/demo_c.pyx', 'cython_hints/c_src/cfib.c'],
        language='c'
    ),
]

TEST_REQUIRE = [
    'pytest',
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    setup_requires=[
        'setuptools>=18.0',
        'cython',
    ],
    extras_require={
        'test': TEST_REQUIRE,
    },
    ext_modules=EXTENSIONS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': ['show_magic=cython_hints.command_line:main'],
    },
)
