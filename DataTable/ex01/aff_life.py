from load_csv import load
import matplotlib.pyplot as plt
from pandas import DataFrame


def display(df: DataFrame) -> None:
    """
    Display received df on a line graph using pyplot.

    The graph has a title, and a legend for each axis.

    In case of any errors, a proper Error message is displayed,
    and -1 is returned.
    """
    try:
        plt.plot(df)

        plt.xticks(range(0, len(df), 40))

        plt.title("Morocco Life Expectancy projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")

        plt.show()

    except Exception as e:
        print("Error:", e)


def main() -> None:
    """
    Load life expectancy data from life_expectancy_years.csv,
    get Morocco's life expectancy, and display it using display()

    In case of any errors, -1 is returned.
    """
    df: DataFrame = load("life_expectancy_years.csv")

    if df is None:
        return

    try:
        display(df.loc["Morocco"])
    except KeyError as e:
        print("KeyError:", e)


if __name__ == "__main__":
    main()
