import json
courses= '{"name" :"KarthikBabu", "languages":["Java","Python"]}'
#Here json is stored as a string variable.
#Parse the content present in Json string
#There is a method available in python called loads which will help me to pass json strings and returns dictionary.
dict_courses= json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
# #Get me the first language taught by trainer.
# list_langauge=dict_courses['languages']
# print(type(list_langauge))
# print(list_langauge[0])
print(dict_courses['languages'][0])

#Parse content present in Json file
with open ('C:\\Users\\karth\\OneDrive\\Documents\\example_1.json')as f:
    data=json.load(f)
    print(data)