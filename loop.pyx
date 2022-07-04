import numpy as np

cimport numpy as np
cimport cython

np.import_array()

DTYPE = float
ctypedef np.float_t DTYPE_t

cdef extern from "foo.h":
    float foo(float)

# @cython.boundscheck(False)
# @cython.wraparound(False)
def loop(np.ndarray[DTYPE_t, ndim=1] v):
    cdef n = v.shape[0]
    cdef np.ndarray[DTYPE_t, ndim=1] out = np.zeros(n, dtype=DTYPE)
    for i in range(n):
        out[i] = foo(v[i])
    return out
