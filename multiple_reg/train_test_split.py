import pandas as pd
from sklearn.model_selection import train_test_split

data=pd.read_csv('profit_dataset.csv')
print(data.head())

# split the data into the training and testing dataset to evaluate the model performance
#  define the dependent varivables and independent varivables

# independent variables
X = data[['R&D Spend', 'Administration', 'Marketing Spend']] 

# dependent varivables
y = data['Profit']

# split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# save the train data in to csv file
X_train.to_csv('X_train.csv', index=False)
y_train.to_csv('y_train.csv', index=False)

# save the testing data in to csv file
X_test.to_csv('X_test.csv', index=False)
y_test.to_csv('y_test.csv', index=False)