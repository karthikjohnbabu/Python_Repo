# importing csv module
import csv
# importing the pandas library
import pandas as pd
# csv file name
filename = "CCG20.csv"
# initializing the titles and rows list
fields = []
rows = []
list= []
from datetime import datetime
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

df = pd.read_csv("CCG20.csv")
if "Status" and "Notes" and "MergeDate" not in df:
    df["Status"] = ""
    df["Notes"] = ""
    df["MergeDate"] = ""
    df.to_csv("CCG20.csv", index=False)

#for row in rows:
    #print()
    #for col in row[9]:
        #x=int(col)
        #print(type(x))
        #print(x,end='')
        #list.append(x)
    #print(list,end='')

col_list = ["Temporary Member ID", "Patient Account Number","Coverage Timeline"]
df = pd.read_csv("CCG20.csv", usecols=col_list)
for index, row in df.iterrows():
    record=(row['Temporary Member ID'], row['Patient Account Number'],row['Coverage Timeline'])
    print(record)
    strdate=record[2]
    #print(strdate)
    mergeddt= strdate.split(';\n')
    #print(mergeddt)
    lstdate=mergeddt[0].split('-') or mergeddt[1].split('-')
    #print(type(lstdate))
    print(lstdate)












