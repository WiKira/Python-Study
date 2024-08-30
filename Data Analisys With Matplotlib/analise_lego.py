import pandas as pd
import matplotlib.pyplot as plt

df_colors = pd.read_csv("./colors.csv")
df_colors

df_colors["name"].nunique()

df_colors["is_trans"].value_counts()

df_sets = pd.read_csv("sets.csv")
df_sets.head()

df_sets["year"].min()

minyear = df_sets["year"].min()
df_sets[df_sets["year"] == minyear]

df_sets.sort_values("year").head(5)

df_sets[df_sets["year"] == minyear].count()

df_sets.nlargest(5, "num_parts")

df_sets.sort_values("num_parts", ascending=False).head(5)

set_by_year = df_sets.groupby("year")["set_num"].count()

set_by_year

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.plot(set_by_year.index[:-2], set_by_year[set_by_year.index[:-2]])

themes_by_year = df_sets.groupby("year").agg({"theme_id": pd.Series.nunique})

themes_by_year.rename(columns={"theme_id" : "nr_themes"}, inplace=True)
themes_by_year

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

themes_by_year.index[:-2]

plt.plot(themes_by_year.index[:-2], themes_by_year[:-2])

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(set_by_year.index[:-2], set_by_year[set_by_year.index[:-2]], color="g")
ax2.plot(themes_by_year.index[:-2], themes_by_year[:-2], color="r")

ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Sets", color="g")
ax2.set_ylabel("Number of Themes", color="r")

parts_per_set = df_sets.groupby("year").agg({"num_parts" : pd.Series.mean})
parts_per_set

plt.scatter(parts_per_set.index[:-2], parts_per_set[:-2])

df_themes = pd.read_csv("themes.csv")
df_themes.head()

df_themes[df_themes["name"] == "Star Wars"]

df_sets[df_sets["theme_id"].isin(df_themes[df_themes["name"] == "Star Wars"]["id"])]

set_theme_count = df_sets["theme_id"].value_counts()
set_theme_count

set_theme_count = pd.DataFrame({"id": set_theme_count.index,
                                "set_count" : set_theme_count.values})
set_theme_count

merged_df = pd.merge(set_theme_count, df_themes, on="id")
merged_df

plt.bar(merged_df["name"][:10], merged_df["set_count"][:10])

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])