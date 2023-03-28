import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root@123')
cur = mydb.cursor()
cur.execute("CREATE DATABASE db1")
