# Numpy Tutorial
# What is NumPy
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# Why Use NumPy
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
This behavior is called locality of reference in computer science.
# Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function.

    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    # Output : 1 2 3 4 5
# Creating Random NumPy Array

    import numpy as np
    
    # Define the shape of the array
    rows = 3
    cols = 4
    # Create a 2D array filled with random integers between 1 and 10
    random_array = np.random.randint(1, 11, size=(rows, cols))
    print("Random 2D Array between 1 and 10:")
    print(random_array)
    #Output : [[ 5  2 10  7]
             [ 3  8  6  4]
             [10  1  2  7]]
# Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).

    import numpy as np
    a = np.array(42)
    b = np.array([1, 2, 3, 4, 5])
    c = np.array([[1, 2, 3], [4, 5, 6]])
    d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    
    print(a.ndim)
    print(b.ndim)
    print(c.ndim)
    print(d.ndim)
    # Output : 0 1 2 3
    #a: 42
    #b: [1 2 3 4 5]
    #c: [[1 2 3]
         [4 5 6]]
    #d: [[[1 2 3]
          [4 5 6]]
         [[1 2 3]
          [4 5 6]]]
# Negative Indexing
Use negative indexing to access an array from the end.

Print the last element from the 2nd dim:

    import numpy as np
    
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    print('Last element from 2nd dim: ', arr[1, -1])
    #Output : 10
    # arr : [[1,2,3,4,5]
            [6,7,8,9,10]]
# Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1    
Slice elements from index 1 to index 5 from the following array:

    import numpy as np

    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[1:5])
    #Output : [2 3 4 5]
From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

    import numpy as np
    
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr[0:2, 1:4])
    # Output : [[2 3 4]
                 [7 8 9]]
# Negative Slicing
Use the minus operator to refer to an index from the end: 

Slice from the index 3 from the end to index 1 from the end:

    import numpy as np
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[-3:-1])
    #The slicing notation arr[-3:-1] extracts elements starting from the third element from the end (inclusive) up to the second element from the end (exclusive).
    #Output : [5 6]
# Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

    import numpy as np
    
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr.shape)
    # Output : (2, 4)
# Reshaping arrays
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.  

Convert the following 1-D array with 12 elements into a 2-D array.

The outermost dimension will have 4 arrays, each with 3 elements:

    import numpy as np

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(4, 3)
    print(newarr)
    # Output : [[ 1  2  3]
                 [ 4  5  6]
                 [ 7  8  9]
                 [10 11 12]]
# Flattening the arrays
Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.  

    import numpy as np

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    newarr = arr.reshape(-1)
    print(newarr)
    # Output : [1 2 3 4 5 6]
# Searching Arrays
You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method

    import numpy as np

    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    x = np.where(arr == 4)
    print(x)
    # Output : (array([3, 5, 6]),)
# Sorting Arrays
Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

The NumPy ndarray object has a function called sort(), that will sort a specified array.

    import numpy as np
    
    arr = np.array([3, 2, 0, 1])
    print(np.sort(arr))
    # Output : [0 1 2 3]
 # To Get the Unique elements from the array
    import numpy as np
    
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    unique_elements = np.unique(a)
    print(unique_elements)
    #Output : [1 2 3 4 5 6]   
