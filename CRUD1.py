import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',password='**********', database='myweb')
# print("Sql Server Connection Id : ",mycon.connection_id)
mycur=mycon.cursor()
print("1. Press 1 for Sign up")
print("2. Press 2 for Sign in")
choice=int(input("Enter your choice : "))
if choice==1:
    name=input("Enter Username : ")
    uid=input("Enter User Id : ")
    pas=input("Enter Password : ")
    q="insert into login values('{}','{}','{}')".format(name,uid,pas)
    mycur.execute(q)
    mycon.commit()
    print("Sign Up is successful...")
elif choice==2:
    uid=input("Login Id : ")
    pas=input("Password : ")
    q="select userid,password from login where userid='{}' and password='{}'".format(uid,pas)
    mycur.execute(q)
    data=mycur.fetchone()
    if data==():
        print("Login Successful....")
    else:
        print("Login Failed! ")

    
    
