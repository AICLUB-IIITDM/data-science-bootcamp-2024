import numpy as np
def create(list):
    # Create a numpy array from this list
    # Return the numpy array
    my_array = np.array(list)
    return my_array
    pass
def convert(list):
  #implement logic here
  arr = np.array(list)
  return arr.reshape(2, -1)
  pass
def common(a,b):
  #implement logic here
  a1 = np.array(a)
  b1 = np.array(b)
  return np.intersect1d(a1,b1)
  pass
def match(a,b):
  #implement logic here
  a1 = np.array(a)
  b1 = np.array(b)
  return np.where(a1==b1)
  pass
def range(a):
  #implement logic here
  a = np.array(a)
  return np.unique(a[(a >= 5) & (a <= 10)])
  pass
def swap(a):
  #implement logic here
  a = np.array(a)
  a[:, [1, 0]] = a[:, [0, 1]]
  return a
  pass
def reverse(arr):
  #implement logic here
  arr = np.array(arr)
  arr = arr[::-1, :]
  return arr
  pass
def replace(arr):
  #implement logic here
  arr = np.array(arr)
  arr[arr % 2 == 1] = -1
  return arr
  pass
def extract(arr):
  #implement logic here
  arr = np.array(arr)
  return arr[arr%2 == 1]
  pass
def remove(a,b):
  #implement logic here
  a = np.array(a)
  b = np.array(b)
  return np.setdiff1d(a,b)
  pass