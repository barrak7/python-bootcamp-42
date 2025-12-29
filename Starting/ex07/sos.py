import sys


def translate(s: str) -> str:
    """
    Translate input string to morse code.

    built-in
    """
    morse_code: dict[int, str] = str.maketrans({
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
        'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
        'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ',
        'Z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ',
        '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ',
        '7': '--... ', '8': '---.. ', '9': '----. ', ' ': '/ '
    })

    s = s.upper()
    result: str = s.translate(morse_code)

    return result.rstrip()


def validate_input(argv: list[str]):
    """
    check if the number of arguments is correct,
    and if input is a valid alphanumeric string
    """
    if len(argv) != 2:
        raise AssertionError

    for c in argv[1]:
        if not c.isalnum() and not c.isspace:
            raise AssertionError


def main():
    """validates input, translates it to morse code, and prints it."""
    try:
        validate_input(sys.argv)
        result: str = translate(sys.argv[1])

        print(result)

    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
