# Conditional Statements in Python

## Introduction
# Welcome to today's lecture on conditional statements in Python. These statements are fundamental for making decisions in your programs based on certain conditions. Let's dive into the world of `if`, `elif`, and `else` statements!

## The "if" Statement
# The basic syntax of an "if" statement is as follows:
age = 18
if age >= 18:
    print("You are eligible to vote.")

## The "if-else" Statement
# The "if-else" statement allows us to execute different code blocks based on whether a condition is true or false.
temperature = 25
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's a pleasant day.")

## The "if-elif-else" Statement
# When dealing with multiple conditions, the "if-elif-else" statement is useful.
num = 0
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

## Nested Conditional Statements
# Conditional statements can be nested inside each other for more complex logic.
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")

## Logical Operators
# Logical operators (`and`, `or`, `not`) can be used to combine multiple conditions.
age = 25
if age >= 18 and age <= 60:
    print("You are eligible to work.")

## Conclusion
# Conditional statements are powerful tools in programming, allowing us to create flexible and responsive code. Understanding their use is crucial for effective Python programming.

## Q&A
# Open the floor for any questions from the audience.
