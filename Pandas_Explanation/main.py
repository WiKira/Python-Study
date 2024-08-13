# with open("weather_data.csv") as file:
#     data = file.readlines()
#     data = [line.strip() for line in data]
#
#
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = [int(row[1]) for row in data if str.isdigit(row[1])]
#
# print(temperatures)
# print(data)

import pandas

data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
#
# print(data_dict)
#
# temp = data["temp"].to_list()
#
# print(temp)
#
# print(round(data["temp"].mean(), 2))
#
# print(data["temp"].max())

# print(data[data['day'] == 'Monday'])
#
# print(data[data['temp'] == data['temp'].max()])
#
# monday = data[data['day'] == 'Monday']
#
# print(monday["condition"])
#
# print((monday["temp"]*9/5)+32)

data_dict = {
    "students": ["Amy" , "James", "Angela"],
    "scores": [76, 56, 65]
}

df = pandas.DataFrame(data_dict)

print(df)

df.to_csv("new_data.csv")
