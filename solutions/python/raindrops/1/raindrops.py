def convert(number):
    """
    Function to add string according to FizzBuzz challenge.
    - If number is divisible by 3, add "Pling",
    - If number is divisible by 5, add "Plang",
    - If number is divisible by 7, add "Plong",
    - If number isn't divisible by 3, 5, or 7, display the number.
    
    :param int number: Number to be checked.
    :return: raindrop sounds.
    :rtype: str
    """
    result = ""
    divisible_3 = False
    divisible_5 = False
    divisible_7 = False
    if number % 3 == 0:
        divisible_3 = True
        result += "Pling"
        
    if number % 5 == 0:
        divisible_5 = True
        result += "Plang"
        
    if number % 7 == 0:
        divisible_7 = True
        result += "Plong"

    if divisible_3 == False and \
    divisible_5 == False and \
    divisible_7 == False:
        result = str(number)
    
    return result
