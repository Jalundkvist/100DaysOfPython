"""
with open('weather_data.csv', mode='r') as data_file:
    data_list = data_file.readlines()
    data = []
    for variables in data:
        new_data = variables.strip()
        data.append(new_d.split(','))
for row in data:
    print(row)
"""
# import csv
# with open('weather_data.csv', mode='r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# maximum = data['temp'].max()
# mean = data['temp'].mean()
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.temp.mul(9/5).add(32))
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_F = monday_temp*9/5+32
# print(monday_temp_F)

# Create dataframe from scratch
data_dict = {"students": ['Amy', 'James', 'Angela'],
             "scores": [76, 56, 65]
             }
df = pandas.DataFrame(data_dict)
df.to_csv("new_data.csv")
print(df)