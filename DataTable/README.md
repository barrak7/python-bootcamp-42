# DataTable
load, manipulate, and display tabular data.

## Ex00: Load my Dataset
load a csv dataset using pandas, print its shape, and return the dataframe.

```py
import pandas as pd

# Loading a csv file using pandas:
df: pd.DataFrame = pd.read_csv("filepath")

# get dataframe shape
print(df.shape)
```

## Ex01: draw my country
using the previous load function, load the life expectancy data, get your countries life expectancy, and display it on a line graph.

learn how to use pandas indexing, and use pyplot to show a graph with a proper title and proper labeling.
```py
# get row with label 'Morocco'
df = df.loc['Morocco']

# display the data frame:
plt.plot(df)

# set the graph title, x ticks, x label, y label
plt.title("Morocco Life Expectancy projections")

plt.xticks(range(0,len(df), 40))
plt.xlabel("Year")
plt.ylabel("Life Expectancy")
```
Result:  
![Morocc life expectancy](./imgs/Morocco_life_expectancy.png)

## Ex02: Compare my Country
Load date on country population, and compare your country's data with some other country.

figure out how to plot multiple lines, manipulate data before plotting, and how to shows a legend and customize the graph.

```py
# slice the data
df = df[:'2050']

# map lambda over values to convert from number abbreviation format to float
f = lambda x: float(x[:-1])

df = df.map(f)

# add label to plot for legend
plt.plot(df, label="Morocco")

# render legend and position it in the lower right corner
plt.legend(loc=4)
```
![Morocco Vs. Taiwan Population](./imgs/population.png)

# Ex03: draw my year
using a scatter plot, show the relationship between GDP and life expectancy for the year 1900 for all the countries.

```py
# load gdp and life expectancy data for year 1900
gdp: DataFrame = load(
    "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
)
life: DataFrame = load("life_expectancy_years.csv")

gdp = gdp.loc[:, '1900']
life = life.loc[:, '1900']

# Scatter plot
plt.scatter(gdp, life)

# set the x axis scale to log scale, set the labels, title, and display the graph
plt.xscale('log')
plt.xticks([300,1000,10000], ['300', '1K', '10K'])

plt.title("1900")
plt.xlabel("Gross domestic product")
plt.ylabel("Life Expectancy")

plt.show()
```
![life expectancy correlation with GDP](./imgs/gdp_life.png)
