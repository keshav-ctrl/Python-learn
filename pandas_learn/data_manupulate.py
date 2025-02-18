import pandas as pd

data = pd.read_csv('record.csv')
# print(data.head())

# to have a look basic strucute of data like number of columns, column name, datatype, 
# print(data.info())

# to view the basic statistics view of data like mean, madian, mode, sd etc
# print(data.describe())

# row filter 
filter_row= data[data["age"]>23]
print(filter_row)

# combine multiple conditions
ft_row = data[(data["age"]>23) & (data["city"] == 'manchester')]
print(ft_row)



