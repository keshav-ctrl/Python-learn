import matplotlib.pyplot as plt
import pandas as pd

y_test = pd.read_csv('y_test.csv', index_col=0)
y_pred = pd.read_csv('y_pred.csv')

plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(),y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')

plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.title("Actual Salary Vs Predicted Salary")
plt.show()