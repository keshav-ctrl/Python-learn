# we can save data frame into the diffent format like csv, excel, json etc using pandas libraties
import pandas as pd

data = {
    "Name" : ['namrata', 'keshave', 'ming', 'keshav', 'suman', 'rohit', 'subash', 'soniya', 'saloni', 'leena'],
    "age" : [30,21,23,24,24,18,19,23,26,25],
    "city" : ['manchester','mumbai','narchyang','pokhara','narchyang','narchyang','narchyang','dana','manchester','manchester']
}

dataFrame = pd.DataFrame(data)
# to save data in the format of csv file
dataFrame.to_csv('record.csv', index=False)
# to save data in the format of excel file if you have the problem to openpyxl then install the openpyxl model using the pip install openpyxl
dataFrame.to_excel('record_excel.xlsx')
# to save data in the format of json file 
dataFrame.to_json('record.json')
print(dataFrame)