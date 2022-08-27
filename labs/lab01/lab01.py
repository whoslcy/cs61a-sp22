def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
        
    product = n
    for i in range(n-1, n-k, -1):
        product *= i
    return product

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    first_digit = y % 10
    sum = first_digit
    y_remaining = y // 10

    while y_remaining != 0:
        digit = y_remaining % 10
        sum += digit
        y_remaining //= 10

    return sum

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    digit1 = n % 10
    n_remaining = n // 10
    if n_remaining == 0:
        return False

    while n_remaining != 0:
        digit2 = n_remaining % 10
        if digit1 == digit2 and digit == 8:
            return True
        digit1 = digit2
        n_remaining //= 10
    
    return False
