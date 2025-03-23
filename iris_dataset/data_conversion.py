import pandas as pd
from sklearn.datasets import load_iris

# load iris dataset
iris = load_iris()

# coversion of data set into the dataframe
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# add the target column (species)
df['species'] = iris.target

# map the target numbers to species names
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# to save the file in csv format
csv_filename = "iris_dataset.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' has been saved successfully")