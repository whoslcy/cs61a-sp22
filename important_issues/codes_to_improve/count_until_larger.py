# https://inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw02/#q1-count-until-larger

def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    "*** YOUR CODE HERE ***"

    if num // 10 == 0:
        return -1

    rightmost_digit = num % 10
    count = 1
    
    num_remaining = num // 10
    while num_remaining != 0:
        digit_to_compare = num_remaining % 10
        if digit_to_compare > rightmost_digit:
            return count
        count += 1
        num_remaining //= 10

    return -1 
