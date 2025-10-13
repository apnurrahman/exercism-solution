def leap_year(year):
    """Function that defines whether the input is a leap year.
    
    :param: year : input
    :return: Boolean
    
    """
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    
    return False
   
