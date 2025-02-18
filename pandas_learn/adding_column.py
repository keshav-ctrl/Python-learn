# adding colunm in the data frame
import pandas as pd

data = {
    "Name" : ['keshave','keshav', 'kashu', 'ming', 'leena','soloni', 'namrata', 'raju', 'mohan','sita'],
    "Age" :[23, 24, 24, 22, 23, 24, 25, 26, 27, 25],
    "Salary" :[50000,60000, 70000, 30000, 50000, 80000,65000,95000,100000,45000],
    "Performance": [85,87,88,83,90,91,89,92,95,85]
}

df = pd.DataFrame(data)
print("Data frame is:")
print(df)
# in pandas there are two types to adding columns
# first method syntan===> df["colunm_name"]= some_data

# I am adding the column name as bonus column and add equation to which add the 10% of the salary column


print("After the adding Bouns column in the data frame:")
df["Bonus"] = df["Salary"] * 0.1
print(df)

# I want again the total salaly that he or she will received so adding new colunm name as Total_Salary
print('The final Data Frame is:')
df["Total_Salary"] = df['Salary'] + df['Bonus']
print(df)


# the second method of adding colunm in the data frame 
# by using intsert()
# df.insert(location, "Column_Name", some_data)

#  I am adding the Employee_Id in the first column in the data set which is auto increment according to 
#  the data frame on increased
df.insert(0,"Employee_Id", range(101, 101+len(df)))
print("the data frame after adding Employee_Id column using insert method")
print(df)

df.to_csv('Employee_Record.csv', index=False)
