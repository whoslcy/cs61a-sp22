def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num == 0:
        return 0
    else:
        digit_to_judge = num % 10
        next_num = num // 10
        if digit_to_judge == prev_digit or digit_to_judge == next_num % 10:
            count = 1
        else:
            count = 0
        return count + neighbor_digits(next_num, digit_to_judge)