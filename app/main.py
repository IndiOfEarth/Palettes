import numpy as np
from numpy.random import random
import random as rnd

# 2d arrays
def arrayplay(input):
    array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    if input == "shape":
        shape = array_2d.shape
        print(f"Array has {shape[0]} rows")
        print(f"Array has {shape[1]} columns")
        for i in range(shape[0]):
            print(array_2d[i])
    elif input == "dimensions":
        print(f"Array has {array_2d.ndim} dimensions")

# tensor = n-dimensional array
def tensorplay(input):
    new_array = np.array(
        [[[1, 2, 3, 4], [5, 6, 7, 8]],
         [[9, 10, 11, 12], [13, 14, 15, 16]],
         [[17, 18, 19, 20], [21, 22, 23, 24]]])
    if input == "shape":
        shape = new_array.shape
        print(f"Array has {shape[0]} dimensions")
        print(f"Array has {shape[1]} rows")
        print(f"Array has {shape[2]} columns")
    elif input == "dimensions":
        print(f"Array has {new_array.ndim} dimensions")

# creating arrays and subsets
def create_array(input, **kwargs):
    if input == "arange":
        new_array = np.arange(rnd.randint(1, 10), rnd.randint(10, 20), 1, dtype=int)
        print(f"array: {new_array}")
    else:
        # creating a random ndim array
        new_array = random((input))
        print(new_array)

    # returns a subset with even spaces between
    subset = kwargs.get("subset")
    if subset == "even":
        subset = np.array(new_array[::2])
        print(f"new subset: {subset}")
    elif subset == "flip":
        subset = np.flip(new_array)
        print(f"new subset: {subset}")

# adding arrays/vectors
def add_array(v1, v2):
    print(v1 + v2)

def multiply_array(v1, v2):
    print(v1 * v2)

# arrayplay("shape")
# tensorplay("shape")
# create_array(input=(2,4,2))

v1 = np.array([[[1,2,3,4],[1,2,3,4]], [[5,6,7,8],[5,6,7,8]]])
v2 = np.array([[[1,2,3,4],[1,2,3,4]], [[5,6,7,8],[5,6,7,8]]])
multiply_array(v1, v2)
