import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

print(df)

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()

clean_df.tail()

clean_df['Starting Median Salary']

clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[43]
clean_df['Undergraduate Major'][43]

clean_df.loc[43]

clean_df['Mid-Career Median Salary']

clean_df['Mid-Career Median Salary'].max()

clean_df['Mid-Career Median Salary'].idxmax()

clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()]

clean_df['Starting Median Salary']

clean_df['Starting Median Salary'].min()

clean_df['Starting Median Salary'].idxmin()

clean_df.loc[clean_df['Starting Median Salary'].idxmin()]

clean_df['Mid-Career Median Salary']

clean_df['Mid-Career Median Salary'].min()

clean_df['Mid-Career Median Salary'].idxmin()

clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

dif_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

dif_col

clean_df.insert(1, 'Spread', dif_col)

clean_df

low_risk = clean_df.sort_values("Spread")
low_risk

high_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)

high_potential.head(5)

high_risk = clean_df.sort_values("Spread", ascending=False)

high_risk.head(5)

high_mid_career = clean_df.sort_values("Mid-Career Median Salary", ascending=False)
high_mid_career.head(5)

clean_df.groupby('Group').count()

pd.options.display.float_format = '{:,.2f}'.format 
clean_df.groupby('Group').mean(numeric_only=True)