"""
    Module that contains function(s) to calculate Collatz Conjecture.
"""

def steps(number):
    """
    Function to count the amount of steps in Collatz Conjecture
    :param int number: input specified number
    :return: the amount of steps taken
    :rtype: int
    """
    iteration = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
        
    while number != 1:
        #even rules
        if number % 2 == 0:
            number /= 2
        #odd rules
        else:
            number = number*3 + 1
        iteration += 1
        
    return iteration