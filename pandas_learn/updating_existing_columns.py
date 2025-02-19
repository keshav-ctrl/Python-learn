import pandas as pd
data = {
    "Name" : ['keshave','keshav', 'kashu', 'ming', 'leena','soloni', 'namrata', 'raju', 'mohan','sita'],
    "Age" :[23, 24, 24, 22, 23, 24, 25, 26, 27, 25],
    "Salary" :[50000,60000, 70000, 30000, 50000, 80000,65000,95000,100000,45000],
    "Performance": [85,87,88,83,90,91,89,92,95,85]
}
df = pd.DataFrame(data)
# df['Salary'] = df['Salary'] * 1.1
# print(df)


df["Salary"] = df['Salary'] * 1.05
print(df)