import sys
from ft_filter import ft_filter
from collections.abc import Callable


def validate_input(s: str):
    """check if string only consists of alphanumeric characters and spaces"""
    for e in s:
        if not e.isalnum() and not e.isspace():
            raise AssertionError


def main():
    """
    Takes in 2 arguments, a string S, and a number N.

    Prints the list of words in S for which len(word) > N is true.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        validate_input(sys.argv[1])
        s: list[str] = sys.argv[1].split()
        n: int = int(sys.argv[2])

        f: Callable[[str], bool] = lambda x: len(x) > n

        filtered = ft_filter(f, s)

        result: list[str] = [item for item in filtered]

        print(result)

    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
