def is_armstrong_number(number):
    """
    Function to determine whether the input is an Armstrong number.

    :param int number: an Armstrong number candidate
    :return: True or False
    :rtype: boolean
    """
    str_number = str(number)
    sum = 0
    len_number = len(str_number)
    for chr in str_number:
        sum += int(chr) ** len_number
    
    # checking value
    if number == sum:
        return True
    return False
