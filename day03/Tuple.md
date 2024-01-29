# Python Tuple

A tuple is created by placing all the items (elements) inside parentheses `()`, separated by commas. A tuple can have any number of items, and they may be of different types (integer, float, list, string, etc.).

### Example:

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```
# Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values. Tuple items are indexed, with the first item having index [0], the second item having index [1], and so on.

1. **Ordered:**
   - When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

2. **Unchangeable:**
   - Tuples are unchangeable, meaning that we cannot change, add, or remove items after the tuple has been created.

3. **Allow Duplicates:**
   - Since tuples are indexed, they can have items with the same value.

To determine how many items a tuple has, use the `len()` function.

### Example:

```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
``````
# Creating a Python Tuple With One Element

In Python, creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is a tuple.

### Example:

```python
var1 = ("Hello")   # This is a string
var2 = ("Hello",)  # This is a tuple with one element

``````
# Type

We can use the `type()` function to determine the class to which a variable or a value belongs.

### Example:

```python
var1 = ("hello")
print(type(var1))  # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>

# Parentheses are optional
var3 = "hello",
print(type(var3))  # <class 'tuple'>
``````
# Access to Tuple Elements

(a) **Indexing:**
   - Like a list, each element of a tuple is represented by index numbers (0, 1, ...) where the first element is at index 0. We can use the index operator `[]` to access an item in a tuple.

### Example:

```python
# Accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0])   # prints "p"
print(letters[5])   # prints "a"
``````

(b) **Negative Indexing:**
   - The index of -1 refers to the last item, -2 to the second last item, and so on. We can use negative indexing to access items from the end of the tuple.

### Example:

```python
# Accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(letters[-1])   # prints 'z'
print(letters[-3])   # prints 'm'
``````
(c) **Slicing:**
   - We can access a range of items in a tuple by using the slicing operator colon `:`.

### Example:

```python
# Accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# Elements beginning to 2nd
print(my_tuple[:-7])  # prints ('p', 'r')

# Elements 8th to end
print(my_tuple[7:])   # prints ('i', 'z')
``````
# Python Tuple Methods

In Python, methods that add items or remove items are not available with tuples. Only the following two methods are available:

### Example:

```python
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# Count the number of occurrences of a specific element
print(my_tuple.count('p'))  # prints 2

# Find the index of the first occurrence of a specific element
print(my_tuple.index('l'))  # prints 3
``````
# Iterating through a Tuple in Python

We can use the `for` loop to iterate over the elements of a tuple.

### Example:

```python
languages = ('Python', 'Swift', 'C++')

# Iterating through the tuple
for language in languages:
    print(language)
``````
# Checking Existence in a Tuple in Python

We use the `in` keyword to check if an item exists in the tuple or not.

### Example:

```python
languages = ('Python', 'Swift', 'C++')

# Checking existence using the 'in' keyword
print('C' in languages)       # False
print('Python' in languages)   # True
``````
# Advantages of Tuple over List in Python

Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list:

1. **Data Type Heterogeneity:**
   - We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.

2. **Immutable Nature:**
   - Tuples are immutable, meaning once a tuple is created, you cannot modify its contents (add, remove, or modify elements). Due to this immutability:
     - Iterating through a tuple is faster than with a list, providing a slight performance boost.
     - Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.

3. **Write-Protection:**
   - If you have data that doesn't change, implementing it as a tuple will guarantee that it remains write-protected.

These advantages make tuples a suitable choice for specific use cases where immutability and performance are crucial.