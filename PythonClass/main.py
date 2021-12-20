Supermarkert ={
    'store1':{
        'name':'Karthik General Store',
         'items':[{'name':'Soap','quantity':20},
                  {'name':'Brush','quantity':30},
                  {'name': 'Pen','quantity':40},]
    },
    'Store 2':{
        'name':'Karthik Book store',
        'items':[{'name':'Python books','quantity':100},
                 {'name':'Django Books','quantity':200},
                 {'name':'Java Books','quantity':300}
        ]
    }
}
#To print the name of store 1.
print(Supermarkert['store1']['name'])#Karthik General Store
print(Supermarkert.get('store1').get('name'))#Karthik General Store

#To print all items present in store 1.
print('The Names all items present in store1')
for d in Supermarkert['store1']['items']:
    print(d['name'])

#How many Django books available?
print('The Number of Django books in store2:')
for d in Supermarkert['Store 2']['items']:
    if d['name']=='Django Books':
        print(d['quantity'])

