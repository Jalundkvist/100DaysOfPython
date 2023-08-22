import pandas

G, C, B = "Gray", "Cinnamon", "Black"
def count_occurrences(lst):
    occurrence_dict = {}
    for fur_color in lst:
        if fur_color in occurrence_dict:
            occurrence_dict[fur_color] += 1
        else:
            occurrence_dict[fur_color] = 1
    return occurrence_dict


df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur = df["Primary Fur Color"]

# What I wanted to do
# list_fur = [x for x in fur.tolist() if not pandas.isnull(x)]
# squirrel_dict = count_occurrences(list_fur)

# Angelas way
gray_squirrel_count = len(df[fur == G])
red_squirrel_count = len(df[fur == C])
black_squirrel_count = len(df[fur == B])


data_dict = {"Fur Color": [G, C, B],
             # "Count": [squirrel_dict["Gray"], squirrel_dict["Cinnamon"], squirrel_dict["Black"]]}
             "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]}

sq_df = pandas.DataFrame(data_dict)
print(sq_df)
