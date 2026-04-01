"""
    Function to count the amount of steps in Collatz Conjecture.
    Two rules applied here:
    - If number is even, divide it by 2.
    - If number is odd, multiply it by 3 and add 1.
    
    :param int number: input specified number
    :return: the amount of steps taken
    :rtype: int
"""

def steps(number):
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