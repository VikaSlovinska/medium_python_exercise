"""
Write a Python function to check if a number is prime.
The function should take an integer as input and return True if the integer is prime and False otherwise.
Hint: A prime number is defined as a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.
To determine if an integer is prime, you can loop through all integers from 2 to the square root of the number (inclusive)
 and check if it is divisible by any of them.
If it is divisible, then it is not prime. If it is not divisible by any of them, then it is prime.
"""

number = 76
def check_prime(num):
    count = 0
    if num > 1:
        for i in range(1, num + 1):
            if (num%i) == 0:
                count = count + 1
    if count == 2:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")


check_prime(44)



