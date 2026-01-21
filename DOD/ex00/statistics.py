from typing import Any
from collections.abc import Callable


def err_wrapper(fun: Callable[[...], Any]) -> Callable[[...], Any]:
    """decorator. wrappes a function within a try except block."""

    def inner(*args: Any, log: bool = True) -> Any:
        """
        Incapsulates callable `fun` in a try-except block.

        if log, it prints `fun.name : result`

        if log, prints `Error` in case of any errors.
        """

        re: Any = None

        try:
            re = fun(*args)

            if log:
                print(fun.__name__, ":", re)
        except Exception:
            if log:
                print("Error")

        return re

    return inner


@err_wrapper
def mean(*args: Any) -> float:
    """calculate the mean of args"""

    n: int = len(args)

    return sum(args) / n


@err_wrapper
def median(*args: Any) -> float:
    """get the median of args"""

    n: int = len(args)
    med: float
    sorted_args: list[float] = sorted(args)
    mid: int = n // 2

    if n % 2:
        med = sorted_args[mid]
    else:
        med = (sorted_args[mid - 1] + sorted_args[mid]) / 2

    return med


@err_wrapper
def quartile(*args: Any) -> list[float]:
    """get the first and third quartile of args"""

    n: int = len(args)
    sorted_args = sorted(args)
    q1: float
    q2: float
    mid: int = n // 2

    if n % 2:
        q1 = median(*sorted_args[: mid + 1], log=False)
    else:
        q1 = median(*sorted_args[:mid], log=False)

    q2 = median(*sorted_args[mid:], log=False)

    if not q1 or not q2:
        raise Exception

    return [q1, q2]


@err_wrapper
def var(*args: Any) -> float:
    """calculate the variance of args"""

    re: float
    n: int = len(args)
    mu: float = mean(*args, log=False)

    dists: list[float] = [(e - mu) ** 2 for e in args]

    re = sum(dists) / n

    return re


@err_wrapper
def std(*args: Any) -> float:
    """calculate the standard deviation of args."""

    re: float
    var_: float = var(*args, log=False)

    re = var_**0.5

    return re


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    calculate statistics of args based on passed kwargs.

    possible kwargs: "mean", "median", "quartile", "std", "var"

    Parameters:
    ----------
    *args: variable number of arguments (numeric values)
    **kwargs: variable number of keyword arguments
    """

    values: set[Any] = set(kwargs.values())

    funcs: dict[str, Callable[[...], Any]] = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "var": var,
        "std": std,
    }

    for func in funcs:
        if func in values:
            funcs[func](*args)
