from load_csv import load
from pandas import DataFrame
import matplotlib.pyplot as plt


def display(gdp: DataFrame, life: DataFrame) -> None:
    """
    Display life expectancy in relation to gdp for year 1900
    using a scatter plot.

    The x scale is set to log scale.

    Parameters:
    -----------
    gdp (DataFrame): gdp for year 1900 for all countries
    life (DataFrame): life expectancy for year 1900 for all countries
    """
    plt.scatter(gdp, life)

    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1K", "10K"])

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.show()


def main() -> None:
    """
    load income_per_person_gdppercapita_ppp_inflation_adjusted.csv and
    life_expectancy_years.csv and display life expectancy in relation
    to gdp in year 1900.
    """
    try:
        gdp: DataFrame = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        life: DataFrame = load("life_expectancy_years.csv")

        gdp = gdp.loc[:, "1900"]
        life = life.loc[:, "1900"]

        display(gdp, life)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
