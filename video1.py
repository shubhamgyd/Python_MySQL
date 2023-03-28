import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='root@123')
print(mydb.connection_id)
