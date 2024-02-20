"""
Write a Python function to find the factorial of a given number.
The factorial of a number n is defined as the product of all integers from 1 up to n.
Hint: You can calculate the factorial of a number using a loop that multiplies each integer from 1 up to the given number.
Alternatively, you can use recursion to calculate the factorial.
The base case is when the input number is 0 or 1, in which case the factorial is 1.
Otherwise, recursively call the function with the argument (n-1) and multiply it by n.
"""

def factorial_iterative(num):
    """Calculate factorial of a number using iteration."""
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

def factorial_recursive(num):
    """Calculate factorial of a number using recursion."""
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        return num * factorial_recursive(num - 1)

# Test the functions
number = 6
print("Factorial of", number, "using iterative method:", factorial_iterative(number))
print("Factorial of", number, "using recursive method:", factorial_recursive(number))

