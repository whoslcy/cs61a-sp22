def match_k(k):
    """
    Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def f(x):
        while x // pow(10, k) != 0:
            if x%10 != x//pow(10,k)%10:
                return False
            x //= 10
        return True
    return f