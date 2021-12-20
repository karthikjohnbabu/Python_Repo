import mysql.connector
#host (Mysql Server name), database, user, password
#conn= mysql.connector.connect(host='localhost', database='APIDevelop',
                        #user='root',password='Passw0rd@221188')
from Backend_utilities.configurations import getConnection

conn=getConnection()
print(conn.is_connected())

cursor=conn.cursor()
cursor.execute('select * from CustomerInfo')
rows=cursor.fetchall()
print(type(rows))
sum=0
for row in rows:
    sum=sum+row[2]
print(sum)

#How to update a record in a table.
query= "update customerInfo set Location =%s where CourseName= %s"
data= ("UK","Jmeter")
cursor.execute(query,data)
conn.commit()
conn.close()