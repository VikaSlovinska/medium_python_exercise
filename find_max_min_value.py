class max_min:
    """A class to find the maximum and minimum values of a given list."""

    def __init__(self, numbers):
        """
        Initializes the max_min class.

        Parameters:
        numbers (list): A list of numbers.
        """
        self.numbers = numbers

    def max(self):
        """
        Finds the maximum value in the list.

        Returns:
        int: The maximum value found in the list.
        """
        numbers = self.numbers
        max_val = numbers[0]
        n = len(numbers)
        for i in range(1, n):
            if numbers[i] > max_val:
                max_val = numbers[i]
        print("Maximum Element ", max_val)

    def min(self):
        """
        Finds the minimum value in the list.

        Returns:
        int: The minimum value found in the list.
        """
        numbers = self.numbers
        min_val = numbers[0]
        n = len(numbers)
        for i in range(1, n):
            if numbers[i] < min_val:
                min_val = numbers[i]
        print("Minimum Element ", min_val)

numbers = [4, 2, 76, 12, 4, 56, 89, 90]
mynum = max_min(numbers)
mynum.max()
mynum.min()



