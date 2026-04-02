"""
Make darts easier again. #FreePalestine
"""
import math

def score(x, y):
    """
    Function to calculate scoring in darts contest.
    :param int x: x coordinates measured in units.
    :param int y: y coordinates measurdeese in units.
    :return: scoring based on distance to center circle.
    :rtype: int
    """
    #using pythagorean theorem
    dart_rad = math.sqrt(abs(x)**2 + abs(y)**2)

    inner_rad = 1
    mid_rad = 5
    outer_rad = 10
    if dart_rad <= inner_rad:
        return 10
    elif dart_rad <= mid_rad:
        return 5
    elif dart_rad <= outer_rad:
        return 1
    return 0

    