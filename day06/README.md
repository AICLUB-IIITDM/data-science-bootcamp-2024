# File Handling and Module Handling in Python

## File Handling

### Introduction:-

In today's tutorial, we'll dive into essential file operations in Python, crucial for handling large datasets in machine learning and data science.

### Opening a File:-

To begin, use the open() function with two arguments: the file name and the open mode.
Common modes include:

1. 'r': Read-only mode
2. 'w': Write-only mode (creates a new file if it doesn't exist)
3. 'a': Append mode (adds output to existing file)
4. 'r+': Read and write mode
5. For binary on Windows, add 'b'.

Code:-

    file1 = open("test.txt")      # equivalent to 'r' or 'rt'
    file1 = open("test.txt",'w')  # write in text mode
    file1 = open("img.bmp",'r+b') # read and write in binary mode

### Reading and Writing Opened Files:-

Python provides versatile methods for file interaction:

1. read(): Reads the entire file, returning a string.
2. readline(): Reads lines and returns a string; fetches line 'n' on the nth call.
3. readlines(): Returns a list with each element as a line from the file.
4. write(): Writes a fixed sequence of characters to a file.
5. writelines(): Writes a list of strings to a file.
6. append(): Appends a string to the file, avoiding overwrite.

Code:-

    # open a file
    file1 = open("test.txt", "r")

    # read the file
    read_content = file1.read()
    print(read_content)

Output:-
    
    This is a test file.
    Hello from the test file.

Code:-

    with open('test2.txt', 'w') as file2:

    # write contents to the test2.txt file
    file2.write('Programming is Fun.')
    file2.write('Programiz for beginners')

Output:-

    Programming is Fun.
    Programiz for beginners

### Copying Files with shutil:-

Utilize the shutil module for file copy operations.  
Example: Using shutil.copy(source, destination) to copy files in Python.

### Deleting Files with shutil.os.remove():

Employ Python's shutil module for file deletion.  
Example: Using shutil.os.remove(file_path) to delete files.

### Closing Files:

After making changes, use the close() method to close the file.  
Ensures changes are saved, releases memory, and prevents further operations.

Code:-
    
        # open a file
        file1 = open("test.txt", "r")
    
        # read the file
        read_content = file1.read()
        print(read_content)
    
        # close the file
        file1.close()

### Handling FileNotFoundError:

When working with files, be cautious about FileNotFoundError.
Avoid by providing correct file paths when creating file objects.


## Module Handling

### Introduction:-

A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code.

Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.

### Creating a Python Module:-

To create a module, write desired code and save it with a .py extension.  
Example: calc.py with add and subtract functions.
    
    # A simple module, calc.py
    def add(x, y):
        return (x+y)
    
    def subtract(x, y):
        return (x-y)

### Importing Modules:-

1. Import using import module.
2. Access functions using the dot (.) operator.

        # importing module calc.py
        import calc

        print(calc.add(10, 2))
        # Output: 12

### From Statements in Python:-

Import specific attributes from a module.  
Example: Importing sqrt and factorial from the math module.

    # importing sqrt() and factorial from the module math
    from math import sqrt, factorial
    
    print(sqrt(16))
    print(factorial(6))
    # Output: 4.0, 720

### Importing All Names:

Use from module_name import * to import all names.  
Caution: May lead to namespace pollution.

    # importing all names from the module math
    from math import *
    
    print(sqrt(16))
    print(factorial(6))
    # Output: 4.0, 720

### Locating Python Modules:

Interpreter searches for modules in specified locations.  
Check current directory, PYTHONPATH, and installation-dependent directories.

    # importing sys module
    import sys
    
    # importing sys.path
    print(sys.path)

### Renaming the Python Module:

Use import Module_name as Alias_name to rename a module.

    # importing sqrt() and factorial from the module math
    import math as mt
    
    print(mt.sqrt(16))
    print(mt.factorial(6))
    # Output: 4.0, 720

### Python Built-in Modules:

Python offers various built-in modules for diverse functionalities.

    # importing built-in module math
    import math
    
    print(math.sqrt(25)) 
    print(math.pi) 
    # ... (examples of math, random, and datetime modules)