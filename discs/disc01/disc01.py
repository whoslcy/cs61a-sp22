from math import sqrt

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining == True:
        return True
    else:
        return False

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return False

def true_func():
    "*** YOUR CODE HERE ***"
    print('Welcome to')

def false_func():
    "*** YOUR CODE HERE ***"
    print('61A')

def is_prime(x):
    """n is a positive integer
    return True if n is a prime number
    return False if n is not a prime number
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 1:
        return False
    
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            return False

    return True

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(1, n+1):
        if i % 3 == 0:
            print('fizz', end='')
        if i % 5 == 0:
            print('buzz', end='')
        if i % 3 and i % 5:
            print(i, end='')
        print()
            
