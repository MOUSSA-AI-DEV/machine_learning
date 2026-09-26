# import pandas as pd
# data=pd.read_csv("data/Clean_Dataset.csv")
# # print(data)
# column=str(input("enter the column that you want count her repetion "))
# word=str(input("enter the word that you want count her repetion "))
# def repeated_word():

#     repeated_in_column = data[column].value_counts()
#     number_of_word = (data[column] == word).sum()

#     return repeated_in_column, number_of_word


# print(repeated_word())
import pandas as pd
data=pd.read_csv("data/Clean_Dataset.csv")
# print(data)

# def repeated_word():
#     word=str(input("enter the word that you want count her repetion "))
#     number_of_word = 0

#     for column in data.columns:
#         for value in data[column]:
#          if word.lower() in str(value).lower():
#             number_of_word += 1

#     return number_of_word


# print(repeated_word())



# from sklearn.preprocessing import OneHotEncoder
# ordinal=[
#     "class",
#     "stops",
# ]
# non_ordinale=[
#     "destination_city",
#     "airline",
#    "source_city",
#    "departure_time",
#    "arrival_time",


# ]




# encoder=OneHotEncoder(
#     handle_unknown="ignore",
#      sparse_output=False
# )


# encoded =encoder.fit_transform(data[non_ordinale])
# print( encoded)
import sys
print(sys.executable)
