from typing import Any
from collections.abc import Callable, Iterable


class ft_filter:
    """
    ft_filter(function or None, iterable) --> ft_filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None,
    return the items that are true.
    """

    def __init__(
        self, f: Callable[[Any], bool] | None, iterable: Iterable[Any]
    ) -> None:
        if not f:
            f = lambda x: bool(x)  # noqa: E731

        self.idx = 0
        self.f = f
        self.valid_items = [item for item in iterable if f(item)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.valid_items):
            res = self.valid_items[self.idx]
            self.idx += 1
            return res

        raise StopIteration
