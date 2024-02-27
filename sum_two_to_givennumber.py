"""
Write a Python program that finds the index of two numbers from a list that add up to a given number.
The program should ask the user to input a list of numbers and the target sum.
Then, it should find the indices of the two numbers in the list that add up to the target sum and return them.
If no such pair is found, the program should return a message saying so. Here are some hints to get you started:

 Create a function called 'find_sum_indices' that takes two parameters: the list of numbers and the target sum.
Inside the find_sum_indices function, use two nested loops to check all possible pairs of numbers in the list.
For each pair of numbers, check if their sum equals the target sum. If it does, return the indices of the pair.
 If no such pair is found after checking all pairs, return a message saying so.
"""


list1 = [2, 5, 5, 11]
target = 10

def find_pair_with_sum(lst, target):
    """
    Find a pair of numbers in the given list that add up to the target sum.

    Args:
    lst (list): The list of numbers to search for pairs.
    target (int): The target sum to find.

    Returns:
    list: A list containing the indices of the pair that adds up to the target sum.
          If no such pair is found, returns None.
    """
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            pair_sum = lst[i] + lst[j+1]
            if pair_sum == target:
                print("Pair found:", lst[i], lst[j+1+i])
                return [i, j+i+1]
    print("No pair found for the given target sum.")
    return None

print(find_pair_with_sum(list1, target))











