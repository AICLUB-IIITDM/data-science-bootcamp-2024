

def tuple_func(my_tuple):
    """
    Takes a tuple as input and performs the following operations:
    1. Slice the tuple to create a new tuple with the last two elements.
    2. Returns the new tuple.
    """
    # Your code for slicing and creating a new tuple goes here
    pass

def dict_func(my_dict):
    """
    Takes a dictionary as input and performs the following operations:
    1. Insert a new key-value pair into the dictionary.
    2. Returns the modified dictionary.
    """
    # Your code for inserting a new key-value pair goes here
    pass

def list_func(my_list):
    """
    Takes a list as input and performs the following operations:
    1. Slice the list to get a sublist excluding the first and last elements.
    2. Returns the sliced list.
    """
    # Your code for slicing the list goes here
    pass

# Initialize the tuple, dictionary, and list
my_tuple =  # Your code to initialize my_tuple goes here
my_dict =  # Your code to initialize my_dict goes here
my_list =  # Your code to initialize my_list goes here

# Demonstrate basic operations
new_tuple = tuple_func(my_tuple)  # Call the function with my_tuple and store the result in new_tuple
modified_dict = dict_func(my_dict)  # Call the function with my_dict and store the result in modified_dict
sliced_list = list_func(my_list)  # Call the function with my_list and store the result in sliced_list

# Testing functions
new_tuple = tuple_func((1, 2, 3, 4, 5))
print("New Tuple:", new_tuple)

modified_dict = dict_func({'a': 1, 'b': 2}, 'c', 3)
print("Modified Dictionary:", modified_dict)

sliced_list = list_func([10, 20, 30, 40, 50])
print("Sliced List:", sliced_list)
