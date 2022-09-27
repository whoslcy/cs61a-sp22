def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"
    distance_from_origin = abs(start)
    if distance_from_origin == k:
        return 1
    elif distance_from_origin < k:
        new_k = k - 1
        return line_stepper(start + 1, new_k) + line_stepper(start - 1, new_k)
