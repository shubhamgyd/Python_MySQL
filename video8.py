import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='db1'
    )

cur=mydb.cursor()
s="DELETE FROM book WHERE title='PHP'"
cur.execute(s)
mydb.commit()
mydb.close()
