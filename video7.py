import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='db1'
    )
cur=mydb.cursor()
s="UPDATE book SET price=price+10 WHERE price>200"
cur.execute(s)
mydb.commit()
mydb.close()
