def square(x: int | float) -> int | float:
    """squares x"""
    return x**2


def pow(x: int | float) -> int | float:
    """raises x to itself"""
    return x**x


def outer(x: int | float, function) -> object:
    """wrappes function in counter that accumulates function(x)"""

    def inner() -> float:
        """
        update count every time executed.
        also, updated `nonlocal` x with function(x) result.
        this way, every time the `function` is called with
        its cumulative operations on `x`
        """
        nonlocal x

        x = function(x)

        return x

    return inner
