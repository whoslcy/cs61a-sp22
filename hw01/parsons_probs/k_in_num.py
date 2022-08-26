def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    True
    >>> k_in_num(2, 123) # .Case 2
    True
    >>> k_in_num(5, 123) # .Case 3
    False
    >>> k_in_num(0, 0) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"

    if num == 0:
        return False

    num_left = num
    # 这样还是不太好，手动 do-while，有重复代码
    separate_digit = num_left % 10
    if separate_digit == k:
        return True
    # the leftover number after the separate_digit was removed
    num_left = num_left // 10

    while num_left != 0:
        separate_digit = num_left % 10
        if separate_digit == k:
            return True
        num_left = num_left // 10
    
    return False
