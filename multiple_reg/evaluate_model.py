import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

y_test = pd.read_csv('y_test.csv')
y_pred = pd.read_csv('y_pred.csv')

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error:{mse}")
print(f"R_Squared: {r2}")