import pandas as pd
from sklearn.linear_model import LinearRegression

X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
X_test = pd.read_csv('X_test.csv')

# initialize the model
model = LinearRegression()

# train the model on the taining data 
model.fit(X_train, y_train)
# predict the test data 
y_pred = model.predict(X_test) 

# Convert predictions to a DataFrame
y_pred_df = pd.DataFrame(y_pred, columns=['Predicted Profit'])


# save the predict data 
y_pred_df.to_csv('y_pred.csv', index=False)
print(y_pred_df.head())