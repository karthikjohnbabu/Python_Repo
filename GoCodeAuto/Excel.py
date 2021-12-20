# importing csv module
import csv
# importing the pandas library
import pandas as pd

# csv file name
filename = "CCG20.csv"
# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%5s" % col),
    print('\n')


df = pd.read_csv("CCG20.csv")
if "AdvancedMD-DateRange" and "Actions" and "Status" and "Remarks" not in df:
    df["AdvancedMD-DateRange"] = ""
    df["Actions"] = ""
    df["Status"] = ""
    df["Remarks"] = ""
    df.to_csv("CCG20.csv", index=False)

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

for row in rows:
    print()
    for col in row[9] and row[11]:
        x=int(col)
        #print(type(x))
        print(x,end='')

