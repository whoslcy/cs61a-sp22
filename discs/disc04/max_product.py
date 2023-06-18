def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    s_length = len(s)
    if s_length == 0:
        return 1
    else:
        max_value = 1
        for i in range(0, s_length):
            new_possible_max = s[i] * max_product(s[i+2:])
            if new_possible_max > max_value:
                max_value = new_possible_max
        return max_value