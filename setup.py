from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "loop",
        sources=["loop.pyx"],
        libraries=["foo"],
        library_dirs=["clib/build/"],
    )
]

setup(
    name="pyclib-test",
    version="0.1.0",
    description="Test vectorisation of c function calls",
    url="https://github.com/deforde/pyclib-test",
    author="Daniel Forde",
    author_email="daniel.forde001@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers :: Researchers",
        "Topic :: Engineering :: Algorithms",
        "License :: Proprietary",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10, <4",
    install_requires=[
        "Cython",
        "numpy",
    ],
    ext_modules=cythonize(ext_modules),
    include_dirs=[numpy.get_include(), "clib"],
)
