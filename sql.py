import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',password='Anant@1987')
mycur=mycon.cursor()
q='show databases'
mycur.execute(q)
lod=mycur.fetchall()
for i in lod:
    print(i)
    