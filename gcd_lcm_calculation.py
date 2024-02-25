"""
Write a Python class that contains methods for finding the greatest common divisor (GCD) and least common multiple (LCM) of a given list of integers.
The class should have two methods: one for finding the GCD and one for finding the LCM.
Hint: To find the GCD, you can use Euclid's algorithm which involves dividing the larger number by the smaller number and
then dividing the remainder by the smaller number until there is no remainder.
The last non-zero remainder is the GCD.
To find the LCM, you can use the fact that LCM(a, b) = (a x b) / GCD(a, b).
You can store the current GCD and LCM as attributes of the class so that they can be updated as needed.
"""
class GCD_LCM:
    """
    A class for computing the greatest common divisor (GCD) and least common multiple (LCM)
    of a given list of integers.
    """

    def __init__(self, numbers):
        """
        Initializes the GCD_LCM class.

        Parameters:
        numbers (list): A list of integers.
        """
        self.numbers = numbers
        self.gcd = self.calculate_gcd()
        self.lcm = self.calculate_lcm()

    def calculate_gcd(self):
        """
        Calculates the greatest common divisor (GCD) of the given list of integers.

        Returns:
        int: The greatest common divisor (GCD).
        """
        # Implementing Euclid's algorithm for GCD calculation
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Initializing the GCD with the first element of the list
        gcd_result = self.numbers[0]

        # Iterating through the list to find the GCD of all numbers
        for num in self.numbers[1:]:
            gcd_result = gcd(gcd_result, num)

        # Returning the final GCD
        return gcd_result

    def calculate_lcm(self):
        """
        Calculates the least common multiple (LCM) of the given list of integers.

        Returns:
        int: The least common multiple (LCM).
        """
        # Defining a function to calculate LCM using GCD
        def lcm(a, b):
            return (a * b) // self.gcd

        # Initializing the LCM with the first element of the list
        lcm_result = self.numbers[0]

        # Iterating through the list to find the LCM of all numbers
        for num in self.numbers[1:]:
            lcm_result = lcm(lcm_result, num)

        # Returning the final LCM
        return lcm_result

# Example usage:
numbers = [12, 18, 24]
gcd_lcm_calculator = GCD_LCM(numbers)
print("GCD:", gcd_lcm_calculator.gcd)
print("LCM:", gcd_lcm_calculator.lcm)



