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
