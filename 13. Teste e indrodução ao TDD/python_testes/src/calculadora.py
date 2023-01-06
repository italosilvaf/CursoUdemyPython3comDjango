def soma0(x, y):
    return x + y


def soma1(x, y):
    assert isinstance(x, (int, float)), 'X precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Y precisa ser int ou float'
    return x + y


def soma2(x, y):
    """ 
    Soma x e y

    >>> soma2(10, 20)
    30

    >>> soma2(100, 200)
    400

    >>> soma2('-10', 20)
    10

    >>> soma2(-10, '20')
    Traceback (most recent call last):
    ...
    AssertionError: Y precisa ser int ou float
    """
    assert isinstance(x, (int, float)), 'X precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Y precisa ser int ou float'
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
