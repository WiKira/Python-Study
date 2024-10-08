# -*- coding: utf-8 -*-
"""Seaborn_and_Linear_Regression_(start).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_a3xrtPThNGMkAmb6_-worX9mfWzNOk4

# Introduction

Do higher film budgets lead to more box office revenue? Let's find out if there's a relationship using the movie budgets and financial performance data that I've scraped from [the-numbers.com](https://www.the-numbers.com/movie/budgets) on **May 1st, 2018**.

<img src=https://i.imgur.com/kq7hrEh.png>

# Import Statements
"""

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.linear_model import LinearRegression

"""# Notebook Presentation"""

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

"""# Read the Data"""

data = pd.read_csv('cost_revenue_dirty.csv')

"""# Explore and Clean the Data

**Challenge**: Answer these questions about the dataset:
1. How many rows and columns does the dataset contain?
2. Are there any NaN values present?
3. Are there any duplicate rows?
4. What are the data types of the columns?
"""

print(f"Shape: {data.shape}")
print("")
print(f"Null Values: {data.isna().values.any()}")
print("")
print(f"Duplicates: ")
print(data.duplicated(subset=["Movie_Title"]).value_counts())
print("")
print(f"Info: ")
print(data.info())
print("")
print(data.head())
print("")
print(data.tail())

"""### Data Type Conversions

**Challenge**: Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format by removing `$` signs and `,`.
<br>
<br>
Note that *domestic* in this context refers to the United States.
"""

data["USD_Production_Budget"] = data["USD_Production_Budget"].str.replace('$', '').str.replace(',', '')
data["USD_Worldwide_Gross"] = data["USD_Worldwide_Gross"].str.replace('$', '').str.replace(',', '')
data["USD_Domestic_Gross"] = data["USD_Domestic_Gross"].str.replace('$', '').str.replace(',', '')

data["USD_Production_Budget"] = pd.to_numeric(data["USD_Production_Budget"])
data["USD_Worldwide_Gross"] = pd.to_numeric(data["USD_Worldwide_Gross"])
data["USD_Domestic_Gross"] = pd.to_numeric(data["USD_Domestic_Gross"])

data

"""**Challenge**: Convert the `Release_Date` column to a Pandas Datetime type."""

data["Release_Date"] = pd.to_datetime(data["Release_Date"])

data

"""### Descriptive Statistics

**Challenge**:

1. What is the average production budget of the films in the data set?
2. What is the average worldwide gross revenue of films?
3. What were the minimums for worldwide and domestic revenue?
4. Are the bottom 25% of films actually profitable or do they lose money?
5. What are the highest production budget and highest worldwide gross revenue of any film?
6. How much revenue did the lowest and highest budget films make?
"""

print(data.describe())

print("Avg Budget")
print(data["USD_Production_Budget"].mean())

print("Avg Worldwide Gross Revenue")
print(data["USD_Worldwide_Gross"].mean())

print("Min Worldwide and Domestic Revenue")
print(data["USD_Worldwide_Gross"].min())
print(data["USD_Domestic_Gross"].min())


lastquartile = data[(data.index.max()//4)*3:]
print("Last quartile")
print(lastquartile["USD_Worldwide_Gross"].sum() - lastquartile["USD_Production_Budget"].sum())

print("Max Bugdet and Max Wordwide Revenue")
print(data.iloc[data["USD_Production_Budget"].idxmax()])
print(data.iloc[data["USD_Worldwide_Gross"].idxmax()])


print("Max Bugdet and Max Wordwide Revenue")
print(data.iloc[data["USD_Production_Budget"].idxmin()])
print(data.iloc[data["USD_Worldwide_Gross"].idxmin()])

print("Revenue by lowest and highest budget")
print(data.iloc[data["USD_Production_Budget"].idxmax()]["USD_Worldwide_Gross"] - data.iloc[data["USD_Production_Budget"].idxmax()]["USD_Production_Budget"])
print(data.iloc[data["USD_Production_Budget"].idxmin()]["USD_Worldwide_Gross"] - data.iloc[data["USD_Production_Budget"].idxmin()]["USD_Production_Budget"])

"""# Investigating the Zero Revenue Films

**Challenge** How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?
"""

films_zero = data[data["USD_Domestic_Gross"] == 0]
films_zero.reset_index(inplace=True)

print(films_zero["Rank"].count())

print(films_zero["USD_Production_Budget"].max())


print(films_zero.iloc[films_zero["USD_Production_Budget"].idxmax()])

"""**Challenge**: How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?"""

films_zero_ww = data[data["USD_Worldwide_Gross"] == 0]
films_zero_ww.reset_index(inplace=True)

print(films_zero_ww.sort_values("USD_Production_Budget", ascending=False))

print(films_zero_ww["Rank"].count())

print(films_zero_ww["USD_Production_Budget"].max())

print(films_zero_ww.iloc[films_zero_ww["USD_Production_Budget"].idxmax()])

"""### Filtering on Multiple Conditions"""

international_releases = data.loc[(data.USD_Domestic_Gross == 0) &
                                  (data.USD_Worldwide_Gross != 0)]
print(len(international_releases))
international_releases.head()

"""**Challenge**: Use the [`.query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) to accomplish the same thing. Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States.

Hint: This time you'll have to use the `and` keyword.
"""

international_query = data.query('USD_Worldwide_Gross > 0 and USD_Domestic_Gross == 0')
print(len(international_query))
international_query.head()

"""### Unreleased Films

**Challenge**:
* Identify which films were not released yet as of the time of data collection (May 1st, 2018).
* How many films are included in the dataset that have not yet had a chance to be screened in the box office?
* Create another DataFrame called data_clean that does not include these films.
"""

# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')

unreleased = data[data["Release_Date"] >= scrape_date]
print(len(unreleased))
unreleased.head()

data_clean = data.drop(unreleased.index)
data_clean

"""### Films that Lost Money

**Challenge**:
What is the percentage of films where the production costs exceeded the worldwide gross revenue?
"""

lost_money = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
print((len(lost_money) / len(data_clean)) * 100)

"""# Seaborn for Data Viz: Bubble Charts"""

plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross',
                     size='USD_Worldwide_Gross')

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')

plt.show()

"""### Plotting Movie Releases over Time

**Challenge**: Try to create the following Bubble Chart:

<img src=https://i.imgur.com/8fUn9T6.png>


"""

plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style('darkgrid'):
  ax2 = sns.scatterplot(data=data_clean,
                     x='Release_Date',
                     y='USD_Production_Budget',
                     hue='USD_Worldwide_Gross',
                     size='USD_Worldwide_Gross')

ax2.set(ylim=(0, 450000000),
        xlim=(data_clean["Release_Date"].min(), data_clean["Release_Date"].max()),
        ylabel='Budget in $100 millions',
        xlabel='Release Date')

plt.show()

"""# Converting Years to Decades Trick

**Challenge**: Create a column in `data_clean` that has the decade of the release.

<img src=https://i.imgur.com/0VEfagw.png width=650>

Here's how:
1. Create a [`DatetimeIndex` object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html) from the Release_Date column.
2. Grab all the years from the `DatetimeIndex` object using the `.year` property.
<img src=https://i.imgur.com/5m06Ach.png width=650>
3. Use floor division `//` to convert the year data to the decades of the films.
4. Add the decades as a `Decade` column to the `data_clean` DataFrame.
"""

dti = pd.DatetimeIndex(data_clean["Release_Date"])
data_clean["Decade"] = (dti.year // 10) * 10

data_clean

"""### Separate the "old" (before 1969) and "New" (1970s onwards) Films

**Challenge**: Create two new DataFrames: `old_films` and `new_films`
* `old_films` should include all the films before 1969 (up to and including 1969)
* `new_films` should include all the films from 1970 onwards
* How many films were released prior to 1970?
* What was the most expensive film made prior to 1970?
"""

old_films = data_clean[data_clean["Decade"] < 1970]
new_films = data_clean[data_clean["Decade"] >= 1970]

print(len(old_films))
print(old_films.iloc[old_films["USD_Production_Budget"].idxmax()])
print(len(new_films))
print(new_films.iloc[new_films["USD_Production_Budget"].idxmax()])

"""# Seaborn Regression Plots"""

sns.regplot(data=old_films,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')

"""**Challenge**: Use Seaborn's `.regplot()` to show the scatter plot and linear regression line against the `new_films`.
<br>
<br>
Style the chart

* Put the chart on a `'darkgrid'`.
* Set limits on the axes so that they don't show negative values.
* Label the axes on the plot "Revenue in \$ billions" and "Budget in \$ millions".
* Provide HEX colour codes for the plot and the regression line. Make the dots dark blue (#2f4b7c) and the line orange (#ff7c43).

Interpret the chart

* Do our data points for the new films align better or worse with the linear regression than for our older films?
* Roughly how much would a film with a budget of $150 million make according to the regression line?
"""

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style('darkgrid'):
  ax3 = sns.regplot(data=new_films,
              x='USD_Production_Budget',
              y='USD_Worldwide_Gross',
                    scatter_kws= {"color": "#2f4b7c", 'alpha': 0.4},
                    line_kws={"color": "#ff7c43"})

ax3.set(ylim=(0, new_films["USD_Worldwide_Gross"].max() * 1.2),
        xlim=(0, new_films["USD_Production_Budget"].max() * 1.2),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $ millions")

"""# Run Your Own Regression with scikit-learn

$$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$
"""

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Find the best-fit line
regression.fit(X, y)

print(regression.intercept_)
print(regression.coef_)

# R-squared
regression.score(X, y)

"""**Challenge**: Run a linear regression for the `old_films`. Calculate the intercept, slope and r-squared. How much of the variance in movie revenue does the linear model explain in this case?"""

X = pd.DataFrame(old_films, columns=["USD_Production_Budget"])
y = pd.DataFrame(old_films, columns=["USD_Worldwide_Gross"])

regression.fit(X, y)

print(regression.intercept_)
print(regression.coef_)
print(regression.score(X, y))

"""# Use Your Model to Make a Prediction

We just estimated the slope and intercept! Remember that our Linear Model has the following form:

$$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$

**Challenge**:  How much global revenue does our model estimate for a film with a budget of $350 million?
"""

budget = 350000000

print(round(22821538.63508039 + 1.64771314 * 350000000, -6))

revenue_estimate = regression.intercept_[0] + regression.coef_[0,0] * budget
revenue_estimate = round(revenue_estimate, -6)
print(revenue_estimate)

print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')

