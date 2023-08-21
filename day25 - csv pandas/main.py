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
