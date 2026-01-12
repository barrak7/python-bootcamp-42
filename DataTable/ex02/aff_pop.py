from load_csv import load
import matplotlib.pyplot as plt
from pandas import DataFrame


def set_yticks(mmax: float, tmax: float) -> None:
    """Set the plot's yticks and labels."""
    max_ = int(max(mmax, tmax))

    ticks: range = range(20, max_, 20)
    labels: list = [f"{i}M" for i in ticks]

    plt.yticks(ticks, labels)


def display(mdf: DataFrame, tdf: DataFrame) -> None:
    """
    Display received dfs on a line graph using pyplot.

    The graph has a title, a legend, and a label for each axis.

    The values are converted to floats.
    Originally, they are a string in the number abbreviation
    format. e.g. 20.3M.

    In case of any errors, a proper Error message is displayed,
    and -1 is returned.
    """
    try:
        mdf = mdf.map(lambda x: float(x[:-1]))
        tdf = tdf.map(lambda x: float(x[:-1]))

        plt.plot(mdf, label="Morocco")
        plt.plot(tdf.values, label="Taiwan")

        plt.legend(loc=4)

        plt.xticks(range(0, len(mdf), 40))

        set_yticks(mdf.max(), tdf.max())

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        plt.show()

    except Exception as e:
        print("Error:", e)


def main() -> None:
    """
    Load population data from population_total.csv,
    get Morocco's data and Taiwan's data and display them
    using display()

    In case of any errors, -1 is returned.

    Variables:
    ----------
    df (DataFrame): all population data
    mdf (DataFrame): Morocco's population data
    tdf (DataFrame): Taiwan's population data
    """
    df: DataFrame = load("population_total.csv")
    mdf: DataFrame
    tdf: DataFrame

    if df is None:
        return

    try:
        mdf = df.loc["Morocco", :"2050"]  # type: ignore[misc]
        tdf = df.loc["Taiwan", :"2050"]  # type: ignore[misc]
        display(mdf, tdf)
    except KeyError as e:
        print("KeyError:", e)


if __name__ == "__main__":
    main()
