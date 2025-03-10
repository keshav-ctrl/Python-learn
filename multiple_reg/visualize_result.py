import matplotlib.pyplot as plt
import pandas as pd

y_test = pd.read_csv('y_test.csv')
y_pred = pd.read_csv('y_pred.csv')

plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(),y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')

plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Actual Profit Vs Predicted Profit")
plt.show()