def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0 or n2 == 0:
        return max(n1, n2)
    else:
        small1, index1 = smallest(n1)
        small2, index2 = smallest(n2)
        # Remove the smallest digit and recurse
        if small1 <= small2:
            mod = 10**index1
            new_n1 = n1 // (10*mod) * mod + n1 % mod
            return small1 + 10*merge(new_n1, n2)
        else:
            mod = 10**index2
            new_n2 = n2 // (10*mod) * mod + n2 % mod
            return small2 + 10*merge(n1, new_n2)


def smallest(x):
    """
    Returns the smallest digit other than 0 in positive integer x together with the index of the smallest digit.
    The rightmost index is 0 and the index increases by 1 each time a left shift is made.

    x: positive integer
    return: (DIGIT, INDEX)
    >>> smallest(321000)
    (1, 3)
    >>> smallest(2)
    (2, 0)
    """
    smallest_digit = 10
    smallest_index = -1
    index = 0
    while True:
        digit = x % 10
        if digit != 0 and digit < smallest_digit:
            smallest_digit = digit
            smallest_index = index
        index += 1
        x //= 10
        if x == 0:
            break
    assert smallest_digit > 0
    assert smallest_index >= 0
    return smallest_digit, smallest_index
