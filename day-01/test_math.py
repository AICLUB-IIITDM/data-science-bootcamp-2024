# Import the add function from the module where it is defined
from math import add  # Replace 'your_module_name' with the actual name of your module

# Define the test function for the add function
def test_add():
    # Test case: Check if add function returns the correct result for given inputs
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(100, 200) == 300
    # Add more test cases as needed
