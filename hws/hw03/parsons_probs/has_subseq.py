def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    # Treat 0 as having no digits
    if seq == 0:
        return True
    else:
        digit_to_locate = seq % 10
        # Next we are going to locate the index of DIGIT_TO_LOCATE in n
        n_iterate = n
        # For storing the index of DIGIT_TO_LOCATE
        target_index = -1
        # index for iteration of N_ITERATE
        i = 0
        while n_iterate != 0:
            rightmost = n_iterate % 10
            if rightmost == digit_to_locate:
                break
            i += 1
            n_iterate //= 10
        # Go deeper if rightmost of *seq* has been found in *n*
        return n_iterate != 0 and has_subseq(n_iterate // 10, seq // 10)