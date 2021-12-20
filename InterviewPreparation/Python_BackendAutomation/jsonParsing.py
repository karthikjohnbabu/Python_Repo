import json
courses = ' {"name" : "Rahulshetty",  "languages" : ["java","python"] } ' # this is a json, and we have stored this json as a string variable.
#The json string can be parsed using the method Loads. And this method loads returns the output as dictionary object.
dict_courses= json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
#get me the first language taught by trainer
print(dict_courses['languages'][0])

#**********Parse content present in Json file.
with open('/Users/karthikbabu/Documents/courses.json') as f:
   data= json.load(f)
   print(data)
   print(type(data))
   print(data['courses'][1]['title'])# Cypress
   print(data['dashboard']['website']) # rahulshettyacademy.com
   #price of course 'RPA'
   print(data['courses'])
   for course in data['courses']:
      print(course)
      if course['title']=='RPA':
         print(course['price'])

with open("/Users/karthikbabu/Documents/courses1.json")as fi:
   data2=json.load(fi)
   assert data == data2

   exampleJSON = (
      ' { "test1":  [ {"lang1": "Java", "lang2": "Python", "other":["fortran", "go", "C"]}  ]   }')











