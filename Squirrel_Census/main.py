import pandas

df = pandas.read_csv("Squirrel_Data.csv")
#
# fur_dict = {}
#
# furs = [x for x in df["Primary Fur Color"].sort_values().unique().tolist() if type(x) == str]
#
# fur_dict["Fur Color"] = furs
#
# qtd = []
#
# for fur in furs:
#     qtd.append(df[df["Primary Fur Color"] == fur]["Primary Fur Color"].count())
#
# fur_dict["Count"] = qtd
#
# print(fur_dict)
#
# data = pandas.DataFrame(fur_dict)
#
# data.to_csv("FursCount.csv")

gray_count = len(df[df["Primary Fur Color"] == "Gray"])
cinnamon_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_count = len(df[df["Primary Fur Color"] == "Black"])

print(gray_count)
print(cinnamon_count)
print(black_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

data = pandas.DataFrame(data_dict)

data.to_csv("FursCount.csv")
