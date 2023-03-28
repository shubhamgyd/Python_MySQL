import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='db1'
    )
cur=mydb.cursor()
s="INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
books=[(2,'PHP',8),(3,'JAVA',10),(3,'DBMS',20)]
cur.executemany(s,books)
mydb.commit()
