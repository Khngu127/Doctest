def sum(numbers):
    """Returns the sum of all numbers in a list with 1 pass and 1 fail
    >>> sum([1,2,3])
    6
    >>> sum([5,8,13])
    25
    """
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()