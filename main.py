#!/usr/bin/env python3

from ctypes import cdll, c_float, POINTER, c_size_t
from random import uniform
import timeit

import numpy as np

from loop import loop

MIN_INPUT_VAL = 0
MAX_INPUT_VAL = 1_000_000
ARRAY_LEN = 500_000
N_ITERATIONS = 100

clib = cdll.LoadLibrary("clib/build/libfoo.so")

func = clib.foo
func.restype = c_float
func.argtypes = [c_float]

funcv = clib.foov
funcv.argtypes = [POINTER(c_float), c_size_t, POINTER(c_float)]

vec_func = np.vectorize(lambda x: func(x))

v = np.array(
    [uniform(MIN_INPUT_VAL, MAX_INPUT_VAL) for _ in range(ARRAY_LEN)], dtype=float
)
v_cfloat = v.astype(c_float)


def raw_loop():
    return np.array([func(x) for x in v])


def vectorised():
    return vec_func(v)


def cythonised():
    return loop(v)


def c_loop():
    out = np.array([0 for _ in range(ARRAY_LEN)], dtype=c_float)
    funcv(
        v_cfloat.ctypes.data_as(POINTER(c_float)),
        ARRAY_LEN,
        out.ctypes.data_as(POINTER(c_float)),
    )
    return out


raw_loop_output = raw_loop()
vectorised_output = vectorised()
cython_output = cythonised()
cloop_output = c_loop()

assert np.equal(raw_loop_output, vectorised_output).all()
assert np.equal(raw_loop_output, cython_output).all()
assert np.equal(raw_loop_output, cloop_output).all()

raw_loop_result = timeit.timeit(raw_loop, number=N_ITERATIONS)
vectorised_result = timeit.timeit(vectorised, number=N_ITERATIONS)
cython_result = timeit.timeit(cythonised, number=N_ITERATIONS)
cloop_result = timeit.timeit(c_loop, number=N_ITERATIONS)

print(f"raw_loop_result = {raw_loop_result}")
print(f"vectorised_result = {vectorised_result}")
print(f"cython_result = {cython_result}")
print(f"cloop_result = {cloop_result}")
