import numpy as np
import pandas as pd


# create  and load the data set

np.random.seed(42)
n_samples = 100

# independent variables
rnd_spend = np.random.randint(100000, 300000, n_samples)
administration = np.random.randint(50000, 500000, n_samples)
marketing_spend = np.random.randint(70000, 200000, n_samples)

# dependent variables
profit = 0.8 * rnd_spend + 0.2 * administration + 0.5 *marketing_spend + np.random.normal(0,5000,n_samples)

# data frame
data = pd.DataFrame(
    {
        'R&D Spend' : rnd_spend,
        'Administration' : administration,
        'Marketing Spend' : marketing_spend,
        'Profit' : profit
    }
)
data.to_csv('profit_dataset.csv', index=False)
print(data.head())
