import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='db1'
    )
cur=mydb.cursor()
s="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(s)



