import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='db1'
    )
cur=mydb.cursor()
s="INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
b1=(1,'Python3',345)
cur.execute(s,b1)
mydb.commit()

