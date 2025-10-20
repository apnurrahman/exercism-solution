def square(number):
    if number <= 0 or number >= 65:
        raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)


def total():
    sum = 0
    for counter in range(1, 65):
        sum += square(counter)

    return sum
        
