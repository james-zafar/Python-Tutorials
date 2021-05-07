""" A gentle introduction to NumPy

    What is NumPy?

    "NumPy brings the computational power of languages like C and Fortran
    to Python, a language much easier to learn and use. With this power
    comes simplicity: a solution in NumPy is often clear and elegant." [1]

    NumPy is the fundamental package for scientific computing in Python. It
    is a Python library that provides a multidimensional array object,
    various derived objects (such as masked arrays and matrices), and an
    assortment of routines for fast operations on arrays, including mathematical,
    logical, shape manipulation, sorting, selecting, basic linear algebra,
    basic statistical operations, and much more. [2]

    At the core of the NumPy package, is the ndarray object. This encapsulates
    n-dimensional arrays of homogeneous data types, with many operations
    being performed in compiled code for performance. [2]

    This file contains a copy of all of the functions discussed during
    the lesson, comparing each NumPy function to an equivalent function
    implemented using core Python only. The python implementation of these
    functions are for demonstration purposes only, and as such do not
    properly handle all edge cases and may not be the most efficient
    implementations. The goal is to show that whilst any NumPy function can
    be converted to core Python, NumPy is often much quicker than any core
    Python implementation as it uses contiguous data types and is unboxed,
    which allows for greater optimisations than is possible with any core
    Python object, for example NumPy can choose to organise data into some
    sort of cache structure or take Python integers and turning them into
    machine integers with specific bit widths which allows it use processor
    level instructions on them.

    Once elements are inside a NumPy array, they are inside a restricted
    computation domain (as NumPy converts them to specific machine types,
    they are fixed bit width integers, no interdependencies between items).
    This allows NumPy to choose most efficient way to do computation; NumPy
    can auto parallelise the operation, use machine level instructions or
    some more sophisticated processor level instructions to vectorise operations.

    Why are Python objects slow?
    Python objects are slow because they are heap allocated and are not
    contiguous, so even if an operation should have some form of locality
    you will not get that as there is no locality with where the objects
    are in the heap.

    References
    ----------

    .. [1] NumPy documentation - https://numpy.org/
    .. [2] What is NumPy? https://numpy.org/doc/stable/user/whatisnumpy.html
"""

import numpy as np
import math

from timer import timer

# Constructing NumPy arrays

# >>> my_arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
# >>> my_arr
# array([[1., 2., 3.],
#        [4., 5., 6.]])
# >>> type(my_arr)
# numpy.ndarray
# >>> my_arr.shape
# (2, 3)

my_array = np.array([10, 20, 30])

# Note data types must be NumPy types, not Python types
my_float_array = np.array([[4, 6, 9],
                           [1, 3, 4]], dtype=np.float32)

# Shape is a tuple of the form (row, columns)
print(my_float_array.shape)

# arr.size is the number of elements in the array across all dimensions,
# my_float_array.size will return 6. This is equivalent of len() on a Python
# list but generalised to compute the length across all dimensions.
print(my_float_array.size)

# We can reshape arrays using np.reshape((x, y)) where (x, y) is a tuple that
# specifies the new dimensions. If we reshape my_float_array with the argument
# (1, 6) then reshaped_array is an array with 1 row and 6 columns, i.e.
# [[4., 6., 9., 1., 3., 4.,]]
reshaped_arr = my_float_array.reshape((1, 6))


def other_useful_functions():
    """ This functions shows some intuitive NumPy functions that are similar to
        operations that can be performed on Python lists, with examples showing
        how to use them. Feel free to change the variable assignment from _ to
        a name to print the values and play around with them.
    """
    example = np.array([[10, 20, 5]])
    other_example = np.array([[20, 40, 10]])
    _ = np.max(example)  # Returns 20.
    _ = np.mean(example)  # Returns 11.666666666666666
    _ = np.min(example)  # Returns 5.
    _ = np.argmin(example)  # returns the index of min value, in this case 2
    _ = example.tolist()  # Convert to a Python list
    _ = np.sort(example)  # returns [[ 5, 10, 20]]
    # We can stack two arrays vertically which concatenates columns
    _ = np.vstack([example, other_example])  # returns [[10, 20,  5], [20, 40, 10]]
    # We can also do the same horizontally to concatenate rows
    _ = np.hstack([example, other_example])  # returns [[10, 20,  5, 20, 40, 10]]

    v_stacked = np.vstack([example, other_example])
    # [[10, 20,  5],
    #  [20, 40, 10]]
    _ = np.sum(v_stacked)  # Returns the sum across all dimensions, in this case 105
    _ = np.sum(v_stacked, axis=0)  # Sum the columns. Returns [30, 60, 15]
    _ = np.sum(v_stacked, axis=1)  # Sum the rows. Returns [35, 70]

    # NumPy also has various rounding functions...
    round_example = np.array([1.2, 5.6, 2.5, 2.94, 1.0003])
    _ = np.round_(round_example, 2)
    _ = np.rint(round_example)
    _ = np.round(round_example)


# Next we will look implement some NumPy functions using core Python and compare
# them for readability and efficiency.

# First, we will compute the sum of a one dimensional array using NumPy and compare
# it to the built in sum() function used for Python lists.

@timer
def compute_np_sum(arg: np.array) -> float:
    sum_ = np.sum(arg)
    # print('Sum of list using numpy:', np_sum)
    return sum_


@timer
def compute_sum_py(arg: list) -> float:
    sum_ = sum(arg)
    # print('Sum of list using numpy:', py_sum)
    return sum_


list_ex = [1, 2, 3, 4, 5, 6]

np_sum = compute_np_sum(np.array(list_ex))
py_sum = compute_sum_py(list_ex)
assert np_sum == py_sum


np_sum = compute_np_sum(np.random.randn(100000))
py_sum = compute_sum_py(list(np.random.randn(100000)))


# NumPy Arrays can be initialised using various methods including, but
# not limited to np.zeros(shape), np.ones(shape), and np.empty(shape).
# We will discuss which of these is the best choice, and compare their
# performance to an implementation using Python lists.

@timer
def initialise_zeros(x: int, y: int) -> np.array:
    zero_initialisation = np.zeros((x, y))
    return zero_initialisation


@timer
def initialise_ones(x: int, y: int) -> np.array:
    one_initialisation = np.ones((x, y))
    return one_initialisation


@timer
def initialise_empty(x: int, y: int) -> np.array:
    empty_initialisation = np.empty((x, y))
    return empty_initialisation


@timer
def initialise_list_py(x: int, y: int, type_: int = 0) -> list:
    arr = []
    for _ in range(x):
        arr.append([type_] * y)

    return arr


np_zeros = initialise_zeros(2500, 2500)
py_zeros = initialise_list_py(2500, 2500)
assert np_zeros.tolist() == py_zeros

np_ones = initialise_ones(2500, 2500)
py_ones = initialise_list_py(2500, 2500, 1)
assert np_ones.tolist() == py_ones

initialise_empty(2500, 2500)


# Next we will compute the l2 distance between two points in two dimensional
# space. This can be achieved easily in NumPy using np.linalg.norm()
@timer
def compute_l2_norm(x: np.array, y: np.array) -> float:
    l2_distance = np.linalg.norm(x - y)
    return l2_distance


@timer
def compute_l2_norm_py(x, y):
    if len(x) != len(y):
        raise ValueError(f'Shapes ({len(x),}) and ({len(y)},) are not aligned')
    dist = math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
    return dist


point_x = [10, 10]
point_y = [8, 9]

np_dist = compute_l2_norm(np.array(point_x), np.array(point_y))
py_dist = compute_l2_norm_py(point_x, point_y)
assert np_dist == py_dist


# We will now look at some more complex examples of how NumPy functions
# simplify complex computations. To compute the dot product of two vectors,
# we can use np.dot(x, y) in NumPy. There is no similar equivalent function
# available in the Python standard library, so we must implement our own.

@timer
def dot_product_np(x: np.array, y: np.array) -> np.array:
    np_dot = np.dot(x, y)
    return np_dot


@timer
def dot_product_py(x, y):
    # Note this is a simplified implementation of np.dot() - we do not deal
    # with broadcasting here, we assume the matrices are of the correct shape.
    # This implementation also assumes the matrices are both two dimensional.
    if len(x) != len(y[0]):
        x_shape = (len(x), len(x[0]))
        y_shape = (len(y), len(y[0]))
        raise ValueError(f'Shapes {x_shape!r} and {y_shape!r} are not aligned!')
    result = [[] for _ in range(len(y[0]))]
    for i, row in enumerate(x):
        for j in range(len(y[1])):
            current_column = [current[j] for current in y]
            row_res = sum([a * b for a, b in zip(row, current_column)])
            result[i].append(row_res)

    return result


mat_a = [[1, 2, 3],
         [4, 5, 6]]
mat_b = [[7, 8],
         [9, 10],
         [11, 12]]

np_res = dot_product_np(np.array(mat_a), np.array(mat_b))
py_res = dot_product_py(mat_a, mat_b)
assert np_res.tolist() == py_res


# What about arithmetic? Most common arithmetic operations on teo vectors
# can be done with the arithmetic operations e.g. a - b, if a and b are
# NumPy arrays will work, and return a NumPy array. In core Python this is
# not so simple and we must validate the shapes of the arrays (lists in Python)
# manually and broadcast them ourselves. We will attempt to implement this using
# core Python to show how some of the functions that look quite simple in NumPy,
# e.g. "a + b" include a lot of behind the scenes logic to make them work efficiently.

def get_shape(arr: list) -> tuple[int, int]:
    rows = 0
    cols = 0
    for dim in arr:
        rows += 1
        if not isinstance(dim, list):
            if rows == 1:
                return tuple((1, 0))
            raise ValueError('Argument is not a valid matrix')
        if cols == 0:
            cols = len(dim)
        elif len(dim) != cols:
            raise ValueError('Can not create matrix from ragged nested sequences')

    return tuple((rows, cols))


def broadcast(arr: list, orig_shape: tuple[int, int], target_shape: tuple[int, int]) -> list:
    if orig_shape == target_shape:
        return arr
    if orig_shape[1] == 0:
        rows = [[arr[0]]] * target_shape[0]
        cols = [row[:] * target_shape[1] for row in rows]
        return cols
    if orig_shape[0] > target_shape[0] or target_shape[0] % orig_shape[0] != 0 or target_shape[1] % orig_shape[1] != 0:
        raise ValueError(f'Operands could not be broadcast together with shapes {orig_shape!r} {target_shape!r}')

    new_arr = []
    if orig_shape[0] != target_shape[0]:
        diff = target_shape[0] - orig_shape[0]
        new_arr = arr[:] * diff
    if orig_shape[1] != target_shape[1]:
        diff = target_shape[1] - orig_shape[1] + 1
        new_arr = [dim[:] * diff for dim in arr]

    return new_arr


@timer
def add_py(x: list, y: list) -> list:
    # Note this Python implementation is specific to sums in two
    # dimensional spaces.
    x_shape = get_shape(x)
    y_shape = get_shape(y)
    y = broadcast(y, y_shape, x_shape)
    new_arr = []
    for idx, row in enumerate(x):
        new_row = [a + b for a, b in zip(row, y[idx])]
        new_arr.append(new_row)

    return new_arr


@timer
def add_np(x: np.array, y: np.array) -> np.array:
    return x + y


original = [[1, 2, 3],
            [4, 5, 6]]
add_element_wise = [[10, 20, 30], [5, 5, 5]]
add_column_wise = [[10], [20]]
add_constant = [50]

py_res = add_py(original, add_constant)
np_res = add_np(np.array(original), np.array(add_constant))
assert py_res == np_res.tolist()

py_res = add_py(original, add_element_wise)
np_res = add_np(np.array(original), np.array(add_element_wise))
assert py_res == np_res.tolist()

py_res = add_py(original, add_column_wise)
np_res = add_np(np.array(original), np.array(add_column_wise))
assert py_res == np_res.tolist()

add_large = np.random.pareto(2, size=(1000, 5))
add_lg = np.random.normal(size=(1000, 1))
py_res = add_py(add_large.tolist(), add_lg.tolist())
np_res = add_np(add_large, add_lg)
assert py_res == np_res.tolist()
