# Try Running These Program in your compiler
[Python Tutorial for Beginners - Learn Python in 5 Hours](https://youtu.be/_uQrJ0TkZlc)
This video, produced by Programming with Mosh, is well-regarded and covers a wide range of Python topics that are essential for beginners.
### 1. Understanding Data Types
```python
# Example for understanding data types

# Integer
int_var = 5
print("Integer:", int_var, "Type:", type(int_var))

# Float
float_var = 3.14
print("Float:", float_var, "Type:", type(float_var))

# String
str_var = "Hello, World!"
print("String:", str_var, "Type:", type(str_var))

# Boolean
bool_var = True
print("Boolean:", bool_var, "Type:", type(bool_var))
```

### 2. Basic Arithmetic Operations
```python
# Example for arithmetic operations

# Addition
add_result = 5 + 3
print("Addition:", add_result)

# Subtraction
sub_result = 5 - 3
print("Subtraction:", sub_result)

# Multiplication
mul_result = 5 * 3
print("Multiplication:", mul_result)

# Division
div_result = 5 / 3
print("Division:", div_result)

# Modulus
mod_result = 5 % 3
print("Modulus:", mod_result)
```

### 3. String Basics
```python
# Example for string basics

my_string = "Hello, Python!"

# Print the length of the string
print("Length of string:", len(my_string))

# First character
print("First character:", my_string[0])

# Last character
print("Last character:", my_string[-1])
```

### 4. String Slicing and Indexing
```python
# Example for string slicing and indexing

my_string = "Hello, Python!"

# First half of the string
first_half = my_string[:len(my_string)//2]
print("First half:", first_half)

# Second half of the string
second_half = my_string[len(my_string)//2:]
print("Second half:", second_half)

# Accessing with negative indexing
last_char = my_string[-1]
print("Last character (negative indexing):", last_char)
```

### 5. String Methods
```python
# Example for string methods

my_string = "Hello, Python!"

# Upper case
print("Upper case:", my_string.upper())

# Lower case
print("Lower case:", my_string.lower())

# Replace
print("Replace 'Python' with 'World':", my_string.replace("Python", "World"))

# Find
print("Position of 'Python':", my_string.find("Python"))

# Split
print("Split by comma:", my_string.split(","))
```

### 6. Concatenation and Formatting
```python
# Example for concatenation and formatting

str1 = "Hello"
str2 = "World"

# Concatenation
concatenated = str1 + " " + str2
print("Concatenated String:", concatenated)

# Formatting
formatted_str = "{} {}!".format(str1, str2)
print("Formatted String:", formatted_str)
```

### 7. Boolean Logic
```python
# Example for boolean logic

bool_var1 = True
bool_var2 = False

# Logical AND
print("AND operation:", bool_var1 and bool_var2)

# Logical OR
print("OR operation:", bool_var1 or bool_var2)

# Logical NOT
print("NOT operation:", not bool_var1)
```

### 8. User Input (Optional)
```python
# Example for user input

# Uncomment these lines to take input from user
# user_str = input("Enter a string: ")
# user_int = int(input("Enter an integer: "))

# For example, let's use these values
user_str = "Hello"
user_int = 5

# Perform a basic operation
print("Concatenating string with integer:", user_str + str(user_int))
```

These examples cover the basic implementation of each task. Students can use these as a guide to understand how to approach and complete the assignment.

## Some Advnaced String Methods

1. **`join()`**:
   - Joins the elements of an iterable (like list, tuple) into a single string. The string on which `join()` is called is used as a separator.
   ```python
   words = ["Hello", "Python", "World"]
   result = " ".join(words)
   print(result)  # Output: "Hello Python World"
   ```

2. **`strip()` / `rstrip()` / `lstrip()`**:
   - Removes whitespaces (or specified characters) from the string. `strip()` removes from both ends, `rstrip()` from the right end, and `lstrip()` from the left end.
   ```python
   text = "   Python   "
   print(text.strip())  # Output: "Python"
   print(text.lstrip()) # Output: "Python   "
   print(text.rstrip()) # Output: "   Python"
   ```

3. **`startswith()` / `endswith()`**:
   - Checks if the string starts or ends with a specified substring.
   ```python
   filename = "example.txt"
   print(filename.endswith(".txt"))  # Output: True
   print(filename.startswith("ex"))  # Output: True
   ```

4. **`isalpha()`, `isdigit()`, `isalnum()`, `isspace()`**:
   - These methods check if the string is all alphabetic, all digit, alphanumeric, or all whitespace, respectively.
   ```python
   print("abc".isalpha())  # Output: True
   print("123".isdigit())  # Output: True
   print("abc123".isalnum())  # Output: True
   print("   ".isspace())  # Output: True
   ```


### `input().split()`

The `input()` function is used to take input from the user as a string. Often, you want to input multiple values in one line, separated by spaces (or another separator). That's where `split()` comes into play.

#### How it works:
- `input()` reads a line from input and returns it as a string.
- `split()` method then splits this string into a list where each word is a list item. The default separator is any whitespace.

#### Example:
```python
# Reads a line from input and splits it into words
input_string = "10 20 30"
numbers = input_string.split()  # Default separator is whitespace
print(numbers)  # Output: ['10', '20', '30']
```

#### Common Usage:
- When you want to input multiple values (like integers or floats) in one line, you first take the string input, then split it into list items.

### `map(list, input().split())`

This is a slightly more complex and less common usage. It's important to note that there's a small error in this expression. The correct form should be `map(function, input().split())`, where `function` is typically `int`, `float`, or another type-casting function.

#### How it works:
- `input().split()` works as explained above.
- `map()` function takes two arguments: a function and an iterable. It applies the function to every item of the iterable.

#### Corrected Example:
```python
# Reads a line from input, splits it, and converts each item to an integer
input_string = "10 20 30"
numbers = list(map(int, input_string.split()))
print(numbers)  # Output: [10, 20, 30]
```

#### Common Usage:
- This pattern is commonly used when you want to input a line of numbers and immediately convert them to integers or floats, instead of keeping them as strings.

#### Key Points to Remember:
- `input().split()` is great for splitting a string input into a list of substrings.
- `map(function, input().split())` takes this a step further by not only splitting the input but also applying a transformation function (like `int` or `float`) to each item in the resulting list.
- It's a common pattern in Python, especially in competitive programming and scripting, where you need to quickly read and process lines of numeric input.



