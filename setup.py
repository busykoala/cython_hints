from setuptools.extension import Extension
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'cython_hints'
VERSION = '0.0.1'
AUTHOR = 'Busykoala'
EMAIL = 'info@busykoala.ch'
DESCRIPTION = 'Demonstrate Cython'
URL = 'https://github.com/busykoala/cython_hints'
REQUIRED = []

# Cython extensions:
# ------------------
# Extension("module", ["module.pyx", "helper.cpp"], language='c++',)
#
EXTENSIONS = [
    Extension('demo_module', sources=['cython_hints/demo_module.pyx'],),
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
    ext_modules=EXTENSIONS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': ['show_magic=cython_hints.command_line:main'],
    },
)
