def steps(number):
    """
    Function to count the amount of steps in Collatz Conjecture.
    Two rules applied here:
    - If number is even, divide it by 2.
    - If number is odd, multiply it by 3 and add 1.
    
    :param int number: input specified number
    :return: the amount of steps taken
    :rtype: int
    """
    steps = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
        
    while number != 1:
        #odd rules
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        steps += 1
        
    return steps