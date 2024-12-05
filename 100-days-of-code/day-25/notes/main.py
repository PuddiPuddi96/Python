# with open(file="../data/weather_data.csv", mode="r") as weather_data_file:
#     lines = weather_data_file.readlines()
#     print(lines)

##############################################################################

# import csv

# with open(file="../data/weather_data.csv", mode="r") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
        
# print(temperatures)

##############################################################################

# import pandas

# data = pandas.read_csv("../data/weather_data.csv")
# #print(data)
# #print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# data_temp_list = data["temp"].to_list()
# print(data_temp_list)

# # average = sum(data_temp_list) / len(data_temp_list)
# # print(round(average, 2))

# print(data["temp"].mean())
# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])

# # Get row with max temperature
# print(data[data.temp == data.temp.max()])

# # Convert tu Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(monday_temp_f)

# # Create a dataframe from scatch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("../data/new_data.csv")

##############################################################################
import pandas

data_to_write = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [0, 0, 0]
}

data = pandas.read_csv("../data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241205.csv")

data_to_write["Count"][0] = len(data[data["Primary Fur Color"] == "Gray"])
data_to_write["Count"][1] = len(data[data["Primary Fur Color"] == "Cinnamon"])
data_to_write["Count"][2] = len(data[data["Primary Fur Color"] == "Black"])

pandas.DataFrame(data_to_write).to_csv("../data/Squirrel_Count.csv")
