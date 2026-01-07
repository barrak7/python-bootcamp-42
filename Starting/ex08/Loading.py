import os


def get_strftime(t: float) -> str:
    """
    format time t to h:m:s:ms

    divide by powers of 60, starting from 60² down to 60⁰,
    to get hours, minutes, seconds.

    At the end, multiply the remainder by 100
    to get the first 2 digits.

    The (bool(curr_t) or bool(result)) term in the loop
    is to make sure that leading zero values aren't included.
    """
    result: str = ''
    div: int = 3600

    result += f"{int(t // div)}:".zfill(3) * (t > 3600)

    t %= div
    div = 60

    result += f"{int(t // div)}:".zfill(3)

    t %= div

    result += f"{int(t)}".zfill(2)

    return result


def format_time(et: float, eta: float, aspi: float) -> str:
    """
    format elasped time, estimated time, and average seconds per iteration
    for tqdm.

    parameters:
    -----------
    et (float): elapsed time in seconds
    eta (float): estimated time in seconds
    aspi (float): average seconds per iteration

    returns:
    --------
    formatted_time (str): formatted time [et<eta, #s/it]
    """
    formatted_time: str

    formatted_time = f"[{get_strftime(et)}<{get_strftime(eta)}," + \
        f" {aspi:>5.2f}s/it]"

    return formatted_time


def get_bar_len(formatted_time: str, tit: int, tw: int) -> int:
    """
    calculate the progress bar length given the terminal width tw,
    and the other variables.

    the constant value 9 is for the fixed characters and spaces.
    """
    bar_len: int = tw - (9 + len(formatted_time) + len(str(tit)) * 2)

    return bar_len


def get_time(st: float, it: int, tit: int) -> tuple[float]:
    """
    Calculate elapsed time, eta, average second per second.

    Parameters:
    -----------
    st (float): starting time
    it (int): current number of iterations
    tit (int): total # of iterations

    Returns:
    --------
    et, eta, aspi: tuple of floats containing elapsed
                   time, eta, and average seconds per iteration
    """
    curr_t: float = os.times().elapsed
    et: float = curr_t - st
    aspi: float = et / it if it else 0
    eta: float = aspi * (tit - it)

    return et, eta, aspi


def print_bar(it: int, tit: int, tw: int, st: float) -> None:
    """
    Prints the progress bar given the current iteration,
    the total # of iterations, starting time, and terminal width.

    Parameters:
    -----------
    it (int): current iteration count
    tit (int): total # of iterations
    tw (int): terminal width
    st (float): execution start time in seconds

    Variables:
    ----------
    et (float): elapsed time in seconds
    eta (float): estimated time in seconds
    aspi (float): average seconds per iteration
    formatted_time (str): formatted time [et<eta, #s/it]
    bar_len (int): length of bar given terminal width and
                   other characters
    pp (int): progress percentage rounded to the nearest integer
    pl (int): progress length rounded to the nearest integer
    """
    et: float
    eta: float
    aspi: float
    formatted_time: str
    bar_len: int
    pp: int
    pl: int

    et, eta, aspi = get_time(st, it, tit)
    formatted_time = format_time(et, eta, aspi)
    bar_len = get_bar_len(formatted_time, tit, tw)
    pp = round(it / tit * 100)
    pl = round(pp * bar_len / 100)

    print(
        f"\r{pp:>3}%|{chr(9608) * pl:<{bar_len}}|" +
        f" {it}/{tit} {formatted_time}",
        end=""
    )


def ft_tqdm(lst: range) -> None:
    """
    tqdm clone. Print a progress bar showing:
        - a percentage of the progress
        - a progress bar
        - # of iterations over total # of iterations
        - elapsed time & ETA
        - average # of seconds per iteration

    Take into account the width of the terminal and the length of the range.
    ETA & average seconds per iteration are updated after each iteration.
    P.S: it assumes that it will only be run in a terminal.

    Variables:
    ----------
    tw (int): terminal width
    tit (int): length of range / total # of iterations
    it (int): current iteration
    st (float): start time

    Params:
    -------
    lst (range): the range over which the progress bar is shown.
    """
    tw: int = os.get_terminal_size().columns
    st: float = os.times().elapsed
    tit: int = len(lst)
    it: int = 0

    print_bar(it, tit, tw, st)

    for i in lst:
        yield i

        it += 1

        print_bar(it, tit, tw, st)

    print()
