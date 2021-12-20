from Backend_utilities.configurations import getQuery


def addBookPayload(isbn):
    body={

"name":"Learn Appium Automation with Python Request",
"isbn":isbn,
"aisle":"2284",
"author":"KJohn Babu"
}
    return body

# So our goal is to create this dictionary dynamically, instead of hard coding the values.

def BuildPayLoadFromDb(query):

    addBody={}
    tp= getQuery(query)
    addBody['name']= tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
