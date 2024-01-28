# Loops and Functions in Python

## Loops

### Introduction:-

In today's tutorial, we'll learn about loops and functions which are the most essential building blocks for your Data science journey, so make sure to learn it properly before moving on complex topics.

### What are Loops in Python

Loops in Python are used to repeatedly execute a block of code. There are two main types of loops in Python: "for" loops and "while" loops. Let's explore both of them with some sample code.

Loops in python are similar to loops in C, except instead of flower brackets we use intendation.(PS if u don't know what intendation is by now, only god can save you.)

I know it sounds boring right? US moment bro..but listen it gets fun.

### "for" Loop

A "for" loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a string, or a range).

Let's see a sample code of all this:

Code :-

    #Example 1: Iterate over a list

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    #Example 2: Iterate over a range

    for i in range(5):
        print(i,end = " ")

    #Example 3: Iterating over dictionary values
    my_dict = {"name": "John", "age": 30}

    for key, value in my_dict.items():
        print(key, value)

Output :-

    #Example 1 :-
        apple
        banana
        cherry

    #Example 2 :-
        1 2 3 4 5

    #Example 3 :-
        name John
        age 30

Explanation :-

In Example 1, the for loop iterates over each element in the fruits list, and the variable fruit takes on each value in the list one by one. The print(fruit) statement is executed for each iteration.

In Example 2, the for loop iterates over a range of numbers from 0 to 4. The print(i) statement is executed for each value of i in the specified range.

Here I wrote end = " " in print statement, what it does is,Generally whenever the loop iterates and prints the value of "i",it automatically prints in new line, but by using end = " "(space),after printing a "i" value instead of going to next line the next value is printed after space,u can experiment with different values like end = "a" etc..

In Example 3,for loop is not only limited to one variable, for example here In each iteration of the loop, the key and value variables are used to unpack the key-value pairs from the tuples returned by my_dict.items(). The key variable will take on the key, and the value variable will take on the corresponding value.

### "while" Loop

A while loop is used to repeatedly execute a block of code as long as a specified condition is true.

Code :-

    #Example: Print numbers from 1 to 5 using a while loop
    counter = 1
    while counter <= 5:
    print(counter)
    counter += 1

Explanation :-

The while loop in the example continues to execute the indented block of code as long as the condition counter <= 5 is true.

Inside the loop, the print(counter) statement prints the current value of counter, and counter += 1 increments the value of counter by 1 in each iteration.

## Functions in Python

Functions in Python are blocks of reusable code that perform a specific task. They help in organizing code, making it modular, and promoting code reuse. Let's explore functions with some small sample codes.

### 1. Basic Function Definition:

Code :-

    # Function definition
    def greet():
    print("Hello, welcome to Python Functions!")

    # Function call
    greet()

Output :-

    Hello, welcome to Python Functions!

Explanation:

Function Definition (def greet():): This line defines a function named greet with no parameters. The colon (:) indicates the start of the function body.

Function Body (print("Hello, welcome to Python Functions!")): The code inside the function is indented. In this case, it prints a welcoming message.

Function Call (greet()): To execute the code inside the function, you call it using its name followed by parentheses. In this case, greet() is called, and the message is printed.

### 2. Functions with Parameters:

Code :-

    # Function definition with parameters
    def square(number):
        result = number ** 2
        print(f"The square of {number} is: {result}")

    # Function call with argument
    square(4)

Output :-

    The square of 4 is: 16

Explanation:

Function Definition (def square(number):): This defines a function named square with a parameter number. The parameter is a placeholder for the actual value that will be passed when the function is called.

Function Body (result = number \*\* 2): Inside the function, the value of number is squared and stored in the variable result.

Function Call (square(4)): The function is called with the argument 4, and the code inside the function is executed using this argument. The result is printed.

### 3. Functions with Return Values:

Code :-

    # Function definition with a return value
    def add(a, b):
        result = a + b
        return result

    # Function call and use of the return value
    sum_result = add(3, 5)
    print(f"The sum is: {sum_result}")

Output :-

    The sum is: 8

Explanation:

Function Definition (def add(a, b):): This defines a function named add with two parameters (a and b).

Function Body (result = a + b): Inside the function, the sum of a and b is calculated and stored in the variable result.

Return Statement (return result): The return statement is used to send the calculated result back to the caller.

Function Call and Use of Return Value (sum_result = add(3, 5)): The function is called with the arguments 3 and 5, and the returned result is stored in the variable sum_result. This result is then printed.

### 4. Default Parameters and Named Arguments:

Code :-

    # Function with default parameter value
    def power(base, exponent=2):
        result = base ** exponent
        print(f"{base} raised to the power {exponent} is: {result}")

    # Function call without providing the second argument
    power(3)
    # Function call with both arguments provided
    power(2, 3)

Output :-

    3 raised to the power 2 is: 9
    2 raised to the power 3 is: 8

Explanation:

Default Parameter (exponent=2): The parameter exponent has a default value of 2. If the caller doesn't provide a value for exponent, it will use the default.

Function Calls:

In the first call (power(3)), only the base argument is provided. The default value for exponent (which is 2) is used.
In the second call (power(2, 3)), both base and exponent values are provided.

## Some more cool things about loops(PS extra but useful information)

### 1.Loop Control Statements:

Python provides two main loop control statements: break and continue.

Code :-

    #Example: Using break and continue in a loop
    for i in range(1, 11):
        if i == 5:
            break  # Exit the loop when i equals 5
        elif i % 2 == 0:
            continue  # Skip even numbers
        print(i)

Explanation :-

In this example, the break statement is used to exit the loop when i equals 5. This means the loop will terminate prematurely.

The continue statement is used to skip the rest of the code inside the loop for the current iteration when i is an even number. The loop will then continue to the next iteration.

### 2.Nested Loops:

Python allows you to nest loops, meaning you can have one loop inside another.

Code :-

    # Example: Nested loops to create a multiplication table

    for i in range(1, 4):
        for j in range(1, 4):
            print(i * j, end=" ")
        print() # Move to the next line after each outer loop iteration

Output :-

    1 2 3
    2 4 6
    3 6 9

Explanation:

In this example, there are two nested for loops. The outer loop (for i in range(1, 6)) iterates over values from 1 to 5, and the inner loop (for j in range(1, 6)) iterates over the same range for each outer loop iteration.

The print(i \* j, end='\t') statement prints the product of i and j with a tab separator. The end='\t' argument in the print function is used to keep the output aligned.

### 3.Loop Else Clause:

Python supports an else clause in loops, which is executed when the loop condition becomes false.

Code :-

    # Example: Using else clause in a loop
    for i in range(1, 3):
        print(i)
    else:
        print("Loop completed successfully!")

Output :-

    1 2 Loop completed successfully!

Explanation:

In this example, the else block is executed after the for loop completes its iterations successfully (i.e., without encountering a break statement). The print("Loop completed successfully!") statement will be executed once the loop finishes.

### 4.Using 'zip' Function :-

The zip function is used to combine elements from multiple iterables like lists into tuples. It returns an iterator that generates tuples containing elements from the input iterables, where the nth tuple contains the nth elements from each of the input iterables.

Simply speaking you can print the values of 2 lists using only a single loop and 2 different variables for both(cool right!)
see the example

Code :-

    # Example: Using zip to print two lists using only one loops
    names = ["Alice", "Bob"]
    ages = [25, 30]

    # Zip the two lists together and iterate over zipped data
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old.")

Output :-

    Alice is 25 years old.
    Bob is 30 years old.

Explanation :-

The zip(names, ages) function creates an iterator that combines elements from the names and ages lists into tuples.

In the for loop, the name and age variables are used to unpack the elements from each tuple, and they are then printed in a formatted string (using f,google more about string formatting).

### 5.Using enumerate Function:

The enumerate function is used to iterate over a sequence (such as a list) while keeping track of the index and the value of each element.

Code :-

    # Example: Using enumerate to iterate over a list with index
    fruits = ["apple", "banana", "cherry"]

    # Enumerate the list to get index and value
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")

Output :-

    Index 0: apple
    Index 1: banana
    Index 2: cherry

Explanation:

The enumerate(fruits) function returns an iterator that produces tuples containing the index and value of each element in the fruits list.

In the for loop, the index and fruit variables are used to unpack the elements from each tuple, and they are then used in the formatted string inside the loop.

## Recursion in python(Good way to understand functions)

Recursion is a programming concept where a function calls itself in order to solve a smaller instance of the same problem. Recursive functions usually have a base case to stop the recursion. Here's a simple example of a recursive function in Python:

Code :-

    # Example: Recursive function to calculate the factorial of a number
    def factorial(n):
        # Base case: factorial of 0 is 1
        if n == 0:
            return 1
        # Recursive case: n! = n * (n-1)!
        else:
            return n * factorial(n - 1)

    # Calculate and print the factorial of 5
    result = factorial(5)
    print("Factorial of 5 is:", result)

![Local Image](recursion.png)

Let's break down the code:

### Function Definition:

Code :-

    def factorial(n):
    This defines a function named factorial that takes one parameter n.

### Base Case:

Code :-

    if n == 0:
        return 1

This is the base case of the recursion. If n is 0, the function returns 1. This is crucial to prevent infinite recursion.

### Recursive Case:

Code :-

    else:
        return n * factorial(n - 1)

If n is not 0, the function calculates n \* factorial(n - 1). This is the recursive step where the function calls itself with a smaller instance of the problem (n - 1).

### Function Call and Output:

Code :-

    result = factorial(5)
    print("Factorial of 5 is:", result)

The function is called with the argument 5. The recursive calls continue until the base case is reached. The final result, in this case, is the factorial of 5, which is then printed.

Output:

Code :-

    Factorial of 5 is: 120

Recursion is a powerful technique, but it's important to handle it with care to avoid stack overflow errors. Ensuring a proper base case and making progress toward it in each recursive call is crucial for the termination of the recursion.
