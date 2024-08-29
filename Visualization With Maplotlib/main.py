import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./QueryResults.csv", header = 0)

df.columns = ['DATE', 'TAG', 'POSTS']

df.columns

df.head()

df.tail()

df.shape

df.count()

df.groupby("TAG").sum(numeric_only=True).idxmax()

df.groupby("TAG").count()["DATE"]

df["DATE"] = pd.to_datetime(df["DATE"])

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df

reshaped_df.shape

reshaped_df.head()

reshaped_df.tail()

reshaped_df.columns

reshaped_df.count()

reshaped_df.fillna(0, inplace=True)

reshaped_df

reshaped_df.isna().values.any()

plt.plot(df[df["TAG"] == "c#"]["DATE"], df[df["TAG"] == "c#"]["POSTS"])

plt.figure(figsize=(16,10)) 
plt.xticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df["java"])
plt.plot(reshaped_df.index, reshaped_df["python"])

plt.figure(figsize=(16,10)) 
plt.xticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16) 

roll_df = reshaped_df.rolling(window=6).mean()
 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16)