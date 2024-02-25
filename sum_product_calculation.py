"""
Write a Python class that contains methods for finding the sum and product of a given list of integers.
The class should have two methods: one for finding the sum and one for finding the product.
Hint: To find the sum, you can use a loop to iterate through each element of the list and add it to a running total.
To find the product, you can use a loop to iterate through each element of the list and multiply it by a running total.
You can store the current sum and product as attributes of the class so that they can be updated as needed.
"""

class list_calculation:
    def __init__(self, nums):
        self.nums = nums
        self.total = 0
        self.total1 = 1
    def sum(self):
        for number in self.nums:
            self.total += number
        print(f"The sum of the numbers is: {self.total}")

    def product(self):
        for number in self.nums:
            self.total1 *= number
        print(f"The product of numbers is: {self.total1}")


numbers = [2, 4, 6, 8, 10]
mycal = list_calculation(numbers)
mycal.sum()
mycal.product()







