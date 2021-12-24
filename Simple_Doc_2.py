import doctest

def multiply(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    >>> multiply(7, 11)
    77
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b

#def add(a, b):
#    """
#    :param a: int
#    :param b: int
#    :return: int
#    >>> add(7, 11)
#    18
#    >>> add('b', 'c')
#    'bc'
#    """
#    return a + b

#def div(a, b):
#    """
#    :param a: int
#    :param b: int
#    :return: int
#    >>> div(33, 3)
#    11
#    >>> div (12, 4)
#    3
#    """
#    return a / b

doctest.testmod()