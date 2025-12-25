import sys


def whatis(args: list[str]) -> None:
    assert len(args) == 2, "more than one argument is provided"

    try:
        num: int = int(args[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    print(("I'm Even.", "I'm Odd.")[num % 2])



if __name__ == "__main__":
    try:
        whatis(sys.argv)
    except AssertionError as e:
        print("AssertionError:",e)
