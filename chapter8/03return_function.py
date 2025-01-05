#In Python, the return value of a function is the result that the function sends back to the part 
#of the program where it was called. The return statement is used in a function to explicitly
#specify the value to be returned.

#Key Points about Return Values:

#(1) A function can return any data type, including numbers, strings, lists, dictionaries, or even other functions.
#(2) If no return statement is specified, the function will return None by default.

def add_numbers(a, b):
    return a + b

# Using the function
result = add_numbers(5, 3)
print("Sum:", result)
