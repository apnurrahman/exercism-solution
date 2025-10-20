def response(hey_bob):
    """
    Function to educate Bob how to answer a statement.
    
    :param str hey_bob: Phrase Bob will respond to.
    :return: Set of phrases according to input.
    :rtype: str
    """
    # Check capitalization and whether it ends with a question mark
    if hey_bob[:len(hey_bob)-1].isupper() == True and hey_bob.endswith("?") == True:
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper() == True:
        return "Whoa, chill out!"
    # Removing any whitespace after last char
    elif hey_bob.rstrip().endswith("?") == True:
        return "Sure."
    # Only whitespace or empty str
    elif hey_bob.isspace() == True or len(hey_bob) == 0:
        return "Fine. Be that way!"
    else:
       return "Whatever."
