import ctypes
import numpy as np
import os


def __getLen(x):
    return ctypes.c_int(len(x))

def __getPointer(x):
    return x.ctypes.data_as(ctypes.c_void_p)


if __name__ == '__main__':
    # load the library
    libcpp = ctypes.CDLL('./library.so')

    # initialize
    a = np.arange(100000, dtype=np.float64)
    b = np.arange(100000, dtype=np.float64)

    # allocate memory for output
    res_c = np.empty_like(a)

    # add the two vectors
    libcpp.add_vector_f64(__getPointer(a), __getPointer(b), __getLen(a), __getPointer(res_c))

    # check correctness
    np.testing.assert_array_equal(res_c, a+b)

    # calculate the mean of a
    libcpp.mean_f64.restype = ctypes.c_double
    mean_a = libcpp.mean_f64(__getPointer(a), __getLen(a))

    # check correctness
    np.testing.assert_equal(mean_a, np.mean(a))

    print('Done!')