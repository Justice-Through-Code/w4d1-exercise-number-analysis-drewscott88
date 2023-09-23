#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):

    # first you need to create a variable 'sum' to 0 since that is where we want to start at
    # then we loop from start to end then add +1 to make it include the end 
    # then we add the sum with each number in the sequence to get our sum_total
    # and finally return the sum_total
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.
    sum = 0
    for num in range(start, end +1):
        sum += num
    return sum

def find_smallest_number(start, end):

    #first we assign smallest_num to the start of the numbers in range
    #then we create a for loop in the range of numbers from start to end +1 so it includes last number
    #then within loop if the number is less than the smallest_num then that number will equalk the smallest in the range
    #and finally we return the smallest_num
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.
    smallest_num = start 
    for num in range(start, end +1):
        if num < smallest_num:
            smallest_num = num
    return smallest_num

def find_largest_number(start, end):

    #first we assign Largest_num to the start of range, then creat loop fro all the numbers in range from start to end +1 to be inclusive
    #then if num is > next num in range it will return the largest_num
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.
    largest_num = start
    for num in range(start, end +1):
        if num > largest_num:
            largest_num = num
    return largest_num

def count_even_numbers(start, end):
    #first we assign count to 0 so the count starts at 0 then start for loop for num in the range from start to end +1 to make in clusive of last num in range
    #then we need to check to see if the numbers are even by seeing if the number is divisible by 2 and keep track of each even number
    #then we return the count of the even numbers
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.
    count_even = 0 
    for num in range(start, end +1):
        if num % 2 ==0:     #I had to get help from chat gpt to figure out how to check for odds and evens
            count_even += 1
    return count_even


def count_odd_numbers(start, end):

    #first we need to assign count to 0 so the range starts at 0 then begin a for loop in the range from atart to end again with +1
    #then we need to check to see if the numbers are odd by seeing if the number is not divisible by two and keep track of all of said numbers
    #return the count of ood numbers
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
    count_odd = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            count_odd += 1
    return count_odd