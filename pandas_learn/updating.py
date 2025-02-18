# updating dataframe using .loc[] method
# syntax df.loc[row_index, "Column_Name"]= new value


import pandas as pd

df = pd.read_csv('Employee_Record.csv')
print(df.head())
# since the once update in the salary in the column it affect the column that dependent 
# so we make a function update_dependent_columns 

def update_dependent_columns(row):
    row["Bonus"] = row["Salary"] * 0.1
    row["Total_Salary"] = row["Salary"] + row["Bonus"]
    return row

df.loc[3,'Salary'] = 50000


# apply the function to update bonus and total salary automatically 
df = df.apply(update_dependent_columns, axis=1)

# back to save the file in csv
df.to_csv('Empolyee_Record.csv', index=False)

print(df)
