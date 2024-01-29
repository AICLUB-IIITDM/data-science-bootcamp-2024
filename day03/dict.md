# Python Dictionaries

Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable, and does not allow duplicates. Dictionaries are written with curly brackets `{}`, and have keys and values. We can find the length of a dictionary by using the `len()` function.

### Example:

```python
# Creating a dictionary
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Printing the dictionary
print(my_dict)
``````
# Valid and Invalid Dictionaries in Python

(a) **Keys of a dictionary must be immutable.** Immutable objects can't be changed once created. Some immutable objects in Python are integer, tuple, and string.

### Example:

```python
# Valid dictionary
# Integer as a key
valid_dict_int = {1: "one", 2: "two", 3: "three"}

# Valid dictionary
# Tuple as a key
valid_dict_tuple = { 
(1, 2): "one two", 3: "three"}
# Invalid dictionary
# Error: Using a list as a key is not allowed
# my_dict = {1: "Hello", [1, 2]: "Hello Hi"}

# Valid dictionary
# String as a key, list as a value
valid_dict_str_list = {"USA": ["Chicago", "California", "New York"]}
``````
Note: Dictionary values can be of any data type, including mutable types like lists.
# Unique Keys in Python Dictionary

(b) **Keys of a dictionary must be unique.** The keys of a dictionary must be unique. If there are duplicate keys, the later value of the key overwrites the previous value.

### Example:

```python
# Creating a dictionary with duplicate keys
hogwarts_houses = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    # Duplicate key with a different house
    "Harry Potter": "Slytherin"
}

# Printing the dictionary
print(hogwarts_houses) #output: {'Harry Potter': 'Slytherin', 'Hermione Granger': 'Gryffindor', 'Ron Weasley': 'Gryffindor'}
``````
# Accessing Dictionary Items in Python

We can access the value of a dictionary item by placing the key inside square brackets.

### Example:

```python
# Creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# Accessing the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London
``````
Note: We can also use the get() method to access dictionary items.
# Adding Items to a Dictionary in Python

We can add an item to a dictionary by assigning a value to a new key.

### Example:

```python
# Creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# Adding an item with "Italy" as the key and "Rome" as its value
country_capitals["Italy"] = "Rome"

# Printing the updated dictionary
print(country_capitals)  # Output: {'Germany': 'Berlin', 'Canada': 'Ottawa', 'Italy': 'Rome'}
``````
# Removing Dictionary Items in Python

We can use the `del` statement to remove an element from a dictionary.

### Example:

```python
# Creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# Deleting an item with the key "Germany"
del country_capitals["Germany"]

# Printing the updated dictionary
print(country_capitals)  # Output: {'Canada': 'Ottawa'}
``````
Note: We can also use the pop() method to remove an item from a dictionary. If we need to remove all items from a dictionary at once, we can use the clear() method.
# Changing Dictionary Items in Python

Python dictionaries are mutable (changeable). We can change the value of a dictionary element by referring to its key.

### Example:

```python
# Creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "London"
}

# Changing the value of the "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

# Printing the updated dictionary
print(country_capitals)  # Output: {'Germany': 'Berlin', 'Italy': 'Rome', 'England': 'London'}
``````
# Iterating Through a Dictionary in Python

We can iterate through dictionary keys one by one using a `for` loop.

### Example:

```python
# Creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# Print dictionary keys one by one
for country in country_capitals:
    print(country)

print()

# Print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital) 
``````
# Python Dictionary Methods
| Method              | Description                                       |
|---------------------|---------------------------------------------------|
| `pop(key)`          | Removes the item with the specified key.          |
| `update(dictionary)`| Adds or changes dictionary items.                 |
| `clear()`           | Removes all the items from the dictionary.        |
| `keys()`            | Returns all the dictionary's keys.                |
| `values()`          | Returns all the dictionary's values.              |
| `get(key)`          | Returns the value of the specified key.           |
| `popitem()`         | Returns the last inserted key and value as a tuple.|
| `copy()`            | Returns a copy of the dictionary.                 |
# Dictionary Membership

We can check whether a key exists in a dictionary by using the `in` and `not in` operators.
###Example:
``````python
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True
``````
Note: The "in" operator checks whether a key exists; it doesn't check whether a value exists or not.