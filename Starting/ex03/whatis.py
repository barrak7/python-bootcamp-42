import sys


def whatis(args: list[str]) -> None:
    assert len(args) == 2, "AssertionError: more than one argument is provided"
    assert args[1].isnumeric() == True, "AssertionError: argument is not an integer"

    num: int = int(args[1])

    print(("I'm Even.", "I'm Odd.")[num % 2])



if __name__ == "__main__":
    try:
        whatis(sys.argv)
    except AssertionError as e:
        print(e)
