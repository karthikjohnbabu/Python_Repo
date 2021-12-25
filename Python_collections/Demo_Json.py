import json
#opening json file
f=open('Sample.json')

#returns Json object as a dictionary
data=json.load(f)
# print(data)

#iterating through the json list
for i in data['emp_details']:
    print(i)

