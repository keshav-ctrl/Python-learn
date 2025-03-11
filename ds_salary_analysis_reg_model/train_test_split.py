import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv('ds_salaries.csv')
# basic knowledge about the data set like mean, median, mode, how many columns and what are they this make sure
# us to basic information about the data set for analysis.
# print(data.describe())
# print(data.info())


# define dependent and independent variables

X = data[['experience_level', 'employment_type', 'job_title', 'company_location', 'company_size']]
y = data['salary_in_usd']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1500)

# to save the in csv format train data
X_train.to_csv('X_train.csv')
y_train.to_csv('y_train.csv')

# to save the csv format test data
X_test.to_csv('X_test.csv')
y_test.to_csv('y_test.csv')