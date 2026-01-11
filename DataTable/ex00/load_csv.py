import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    load csv file using pandas.

    Exceptions are handled gracefully.
    A proper error message is displayed, and None is returned.

    Parameters:
    ----------
    path (str): the relative or full path of the csv file.

    Returns:
    --------
    df (pd.DataFrame): pandas DataFrame with the contents of the file.
    """
    df: pd.DataFrame = None

    try:
        df = pd.read_csv(path, index_col=0)

        print("Loading dataset of dimensions", df.shape)
    except Exception as e:
        print("Error:", e)

    return df
