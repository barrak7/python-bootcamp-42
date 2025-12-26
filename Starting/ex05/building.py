import sys


def building(input_: str) -> None:
    """
    Counts number of lower case, upper case characters,
    punctuation marks, spaces, and digits in user input.

    Uses buit-in truth methods to detect category of character.
    For punctuation marks, we use `in` operator over list of punctuations.

    After counting, it prints the length of the string,
    and the count of each category on a seperate line.

    Parameters
    ----------
    input_ (str): user input

    Variables:
    ----------
    n (int): string length
    ul (int): uppercase letters counter
    ll (int): lowercase letters counter
    pm (int): punctuation marks counter
    sp (int): space counter
    dj (int): digits counter
    """
    n: int = len(input_)
    ul: int = 0
    ll: int = 0
    pm: int = 0
    sp: int = 0
    dj: int = 0

    for c in input_:
        ul += c.isupper()
        ll += c.islower()
        pm += c in """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
        sp += c.isspace()
        dj += c.isdigit()

    print(f"The text contains {n} characters:")
    print(f"{ul} upper letters")
    print(f"{ll} lower letters")
    print(f"{pm} punctuation marks")
    print(f"{sp} spaces")
    print(f"{dj} digits")


def main():
    """
    Check if user passes arguments.
    If more than one, print AssertionError.
    If no argument is passed, ask user for input.

    User input is read from stdin.
    If it doesn't end with a newline, a newline is printed
    to seperate script output from user input on display.

    Call building function with user input.
    """
    input_ = ""

    if len(sys.argv) > 2:
        print("AssertionError: More than one arguments provided.")
        return 0

    if len(sys.argv) < 2:
        print("What is the text to count?")
        with open(0) as f:
            input_ += f.read()
        if input_[-1] != "\n":
            print()
    else:
        input_ = sys.argv[1]

    building(input_)


if __name__ == "__main__":
    main()
