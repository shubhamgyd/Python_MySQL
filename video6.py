import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='db1'
    )
cur=mydb.cursor()
s="SELECT * FROM book"
cur.execute(s)
result=cur.fetchall()
for rec in result:
    print(rec)
mydb.close()
