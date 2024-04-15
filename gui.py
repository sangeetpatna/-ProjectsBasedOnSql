from tkinter import *
import mysql.connector as sql
sqlcon=sql.connect(host="localhost",user="root",password="********",database="hubnet")
sqlcur=sqlcon.cursor()
from tkinter import messagebox

from PIL import ImageTk,Image 
win=Tk()
win.geometry("1000x700+250+50")
win.title("HSMS")
win.resizable(0,0)
win.config(background='chocolate')
def SignUp():
    suwin=Tk()
    suwin.geometry("1000x700+250+50")
    suwin.title("HSMS")
    suwin.resizable(0,0)
    suwin.config(background='chocolate')
    suwin.iconbitmap("C:\\Users\\Anant\\Desktop\\logo.ico")
    def Submit():
        na=ent1.get()
        uid=ent2.get()
        pas=ent3.get()
        q="insert into login values('{}','{}','{}')".format(na,uid,pas)
        sqlcur.execute(q)
        sqlcon.commit()
        messagebox.showinfo("SignUp","SignUp done successfully......")
        suwin.destroy()
    def Reset():
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
    def Close():
        suwin.destroy()    
    label3=Label(suwin,text="\tWelcome To Hubnet Student Management System\t    ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
    label3.place(x=2,y=3)
    label4=Label(suwin,text="  Website Address: 'www.hubnettech.net'      Mob-No. : 8589848785   ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
    label4.place(x=2,y=647)
    but2=Button(suwin,text="Sign In ",font=24,fg="maroon",bg="silver",bd="10",command=SignIn)
    but2.place(x=898,y=62)
    label5=Label(suwin,text="HUBNET USER SIGNUP FORM", font=("algerian",30,"bold","underline"),bg="chocolate",fg="silver")
    label5.place(x=230,y=72)
    label6=Label(suwin,text="Name        : ",font=("monotype corsiva",25,"bold"),bg="chocolate",fg="silver")
    label6.place(x=120,y=180)
    label6=Label(suwin,text="User Id     : ",font=("monotype corsiva",25,"bold"),bg="chocolate",fg="silver")
    label6.place(x=120,y=320)
    label6=Label(suwin,text="Password  : ",font=("monotype corsiva",25,"bold"),bg="chocolate",fg="silver")
    label6.place(x=120,y=460)       
    name=StringVar()
    userid=StringVar()
    password=StringVar()
    na=name.get()
    uid=userid.get()
    pas=password.get()
    ent1=Entry(suwin,font=("monotype corsiva",23),fg="maroon",bg="silver",width=37,bd=3,textvariable=name)
    ent1.place(x=350,y=180)
    ent2=Entry(suwin,font=("monotype corsiva",23),fg="maroon",bg="silver",width=30,bd=3,textvariable=userid)
    ent2.place(x=350,y=320)
    fix_ent=Entry(suwin,font=("monotype corsiva",25,"bold"),bg="silver",fg="maroon",width=8,bd=3)
    fix_ent.place(x=800,y=320)
    fix_ent.insert(0,"@hub.net")
    fix_ent.config(state="readonly")
    ent3=Entry(suwin,font=("monotype corsiva",23),fg="maroon",bg="silver",width=37,bd=3,textvariable=password)
    ent3.place(x=350,y=460)
    but2=Button(suwin,text=" Submit ",font=24,fg="maroon",bg="silver",bd="10",command=Submit)
    but2.place(x=300,y=550)
    but3=Button(suwin,text=" Reset ",font=24,fg="maroon",bg="silver",bd="10",command=Reset)
    but3.place(x=452,y=550)
    but4=Button(suwin,text=" Close ",font=24,fg="maroon",bg="silver",bd="10",command=Close)
    but4.place(x=600,y=550)
    
def SignIn():
    siwin=Tk()
    siwin.geometry("1000x700+250+50")
    siwin.title("HSMS")
    siwin.resizable(0,0)
    siwin.config(background='chocolate')
    siwin.iconbitmap("C:\\Users\\Anant\\Desktop\\logo.ico")
    label7=Label(siwin,text="\tWelcome To Hubnet Student Management System\t    ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
    label7.place(x=2,y=3)
    label8=Label(siwin,text="  Website Address: 'www.hubnettech.net'      Mob-No. : 8589848785   ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
    label8.place(x=2,y=647)
    label9=Label(siwin,text="Login Window", font=("algerian",35,"bold","underline"),bg="chocolate",fg="silver")
    label9.place(x=380,y=82)
    label10=Label(siwin,text="User Id     : ",font=("monotype corsiva",25,"bold"),bg="chocolate",fg="silver")
    label10.place(x=120,y=220)
    label11=Label(siwin,text="Password  : ",font=("monotype corsiva",25,"bold"),bg="chocolate",fg="silver")
    label11.place(x=120,y=360)
    def exit():
        siwin.destroy()
    def Reset():
        ent2.delete(0,END)
        ent3.delete(0,END)
    def check_credential():
        uid=ent2.get()
        pas=ent3.get()
        q="select userid,password from login where userid='{}' and password='{}'".format(uid,pas)
        sqlcur.execute(q)
        data=sqlcur.fetchall()
        if data==[]:
            messagebox.showinfo("SignIn","Login Fail due to invalid entry!")
        else:
            crudwin=Tk()
            crudwin.geometry("1000x700+250+50")
            crudwin.title("HSMS")
            crudwin.resizable(0,0)
            crudwin.config(background='chocolate')
            crudwin.iconbitmap("C:\\Users\\Anant\\Desktop\\logo.ico")
            
            def SearchRec():
                    id =sid.get()
                    q="select * from stu_info where sid='{}'".format(id)
                    sqlcur.execute(q)
                    record=sqlcur.fetchone()
                    if record!=[]:
                        print(record)
                        messagebox.showinfo("Search","Record found")
                    else:
                        messagebox.showinfo("Search","Record Not found")
                    
            def InsertRec():
                id =sid.get()
                sn=sname.get()
                ph=phone_no.get()
                cn=cname.get()
                tf=fees.get()
                db=dob.get()
                da=doa.get()
                q="insert into stu_info values('{}','{}','{}','{}','{}','{}','{}')".format(id,sn,ph,cn,tf,db,da)
                sqlcur.execute(q)
                sqlcon.commit()
                messagebox.showinfo("NEW Entry","New Record added successfully......")
                
            def UpdateRec():
                id =sid.get()
                sn=sname.get()
                ph=phone_no.get()
                cn=cname.get()
                tf=fees.get()
                db=dob.get()
                da=doa.get()
                q="insert into login values('{}','{}','{}','{}','{}','{}','{}')".format(id,sn,ph,cn,tf,db,da)
                sqlcur.execute(q)
                sqlcon.commit()
                messagebox.showinfo("NEW Entry","New Record added successfully......")
                
            def DeleteRec():
                id =sid.get()
                q="delete from stu_info where sid='{}'".format(id)
                sqlcur.execute(q)
                sqlcon.commit()
                messagebox.showinfo("Record","Record deleted successfully......")
                
            def sidFocIn (event):
                if sid.get()=="Enter Student's Id Number":
                    sid.delete(0,END)
                    sid.config(bg="silver",fg="maroon")                       
            def snameFocIn (event):
                if sname.get()=="Enter Student's Full Name":
                    sname.delete(0,END)
                    sname.config(bg="silver",fg="maroon")
            def phoneFocIn (event):
                if phone_no.get()=="Enter Student's Phone Number":
                    phone_no.delete(0,END)
                    phone_no.config(bg="silver",fg="maroon")
            def cnameFocIn (event):
                if cname.get()=="Enter Course Name":
                    cname.delete(0,END)
                    cname.config(bg="silver",fg="maroon")
            def feesFocIn (event):
                if fees.get()=="Enter Total Fee Amount":
                    fees.delete(0,END)
                    fees.config(bg="silver",fg="maroon")
                    
            def dobFocIn (event):
                if dob.get()=="Enter Student's Date of Birth":
                    dob.delete(0,END)
                    dob.config(bg="silver",fg="maroon")
            def doaFocIn (event):
                if doa.get()=="Enter Date of Admission":
                    doa.delete(0,END)
                    doa.config(bg="silver",fg="maroon")
            
            def sidFocOut (event):
                if sid.get=='':
                    sid.insert(0,"Enter Student's Id Number")
                    sid.config(bg="silver",fg="maroon")
            def snameFocOut (event):
                if sname.get=='':
                    sname.insert(0,"Enter Student's Full Name")
                    sname.config(bg="silver",fg="maroon")
            def phoneFocOut(event):
                if phone_no.get()=='':
                    phone_no.insert(0,"Enter Student's Phone Number")
                    phone_no.config(bg="silver",fg="maroon")
            def cnameFocOut (event):
                if cname.get()=='':
                    cname.insert(0,"Enter Course Name")
                    cname.config(bg="silver",fg="maroon")
            def feesFocOut(event):
                if fees.get()=='':
                    fees.insert(0,"Enter Total Fee Amount")
                    fees.config(bg="silver",fg="maroon")
            def dobFocOut (event):
                if dob.get()=='':
                    dob.insert(0,"Enter Student's Date of Birth")
                    dob.config(bg="silver",fg="maroon")
            def doaFocOut(event):
                if doa.get()=='':
                    doa.insert(0,"Enter Date of Admission")
                    doa.config(bg="silver",fg="maroon")
                
            label7=Label(crudwin,text="\tWelcome To Hubnet Student Management System\t    ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
            label7.place(x=2,y=3)
            label8=Label(crudwin,text="  Website Address: 'www.hubnettech.net'      Mob-No. : 8589848785   ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
            label8.place(x=2,y=647)
            label9=Label(crudwin,text=" CRUD OERATION ",font=("algerian",30,"bold","underline"),bg="chocolate",fg="silver")
            label9.place(x=330,y=90)
            sid=Entry(crudwin,font=("monotype corsiva",20),fg="maroon",bg="silver",width=55,bd=5)
            sid.place(x=165,y=170)
            sname=Entry(crudwin,font=("monotype corsiva",20),fg="maroon",bg="silver",width=55,bd=5)
            sname.place(x=165,y=220)
            phone_no=Entry(crudwin,font=("monotype corsiva",20),fg="maroon",bg="silver",width=55,bd=5)
            phone_no.place(x=165,y=270)
            cname=Entry(crudwin,font=("monotype corsiva",20),fg="maroon",bg="silver",width=55,bd=5)
            cname.place(x=165,y=320)
            fees=Entry(crudwin,font=("monotype corsiva",20),fg="maroon",bg="silver",width=55,bd=5)
            fees.place(x=165,y=370)
            dob=Entry(crudwin,font=("monotype corsiva",20),fg="maroon",bg="silver",width=55,bd=5)
            dob.place(x=165,y=420)
            doa=Entry(crudwin,font=("monotype corsiva",20),fg="maroon",bg="silver",width=55,bd=5)
            doa.place(x=165,y=470)
            sid.insert(0,"Enter Student's Id Number")
            sid.bind('<FocusIn>',sidFocIn)
            sid.bind('<FocusOut>',sidFocOut)
            sname.insert(0,"Enter Student's Full Name")
            sname.bind('<FocusIn>',snameFocIn)
            sname.bind('<FocusOut>',snameFocOut)
            phone_no.insert(0,"Enter Student's Phone Number")
            phone_no.bind('<FocusIn>',phoneFocIn)
            phone_no.bind('<FocusOut>',phoneFocOut)
            cname.insert(0,"Enter Course Name")
            cname.bind('<FocusIn>',cnameFocIn)
            cname.bind('<FocusOut>',cnameFocOut)
            fees.insert(0,"Enter Total Fee Amount")
            fees.bind('<FocusIn>',feesFocIn)
            fees.bind('<FocusOut>',feesFocOut)
            dob.insert(0,"Enter Student's Date of Birth")
            dob.bind('<FocusIn>',dobFocIn)
            dob.bind('<FocusOut>',dobFocOut)
            doa.insert(0,"Enter Date of Admission")
            doa.bind('<FocusIn>',doaFocIn)
            doa.bind('<FocusOut>',doaFocOut)
            but1=Button(crudwin,text="SearchRec",font=24,fg="maroon",bg="silver",bd="20",command=SearchRec)
            but1.place(x=170,y=550)
            but2=Button(crudwin,text="InsertRec",font=24,fg="maroon",bg="silver",bd="20",command=InsertRec)
            but2.place(x=350,y=550)
            but3=Button(crudwin,text="UpdateRec",font=24,fg="maroon",bg="silver",bd="20")
            but3.place(x=515,y=550)
            but4=Button(crudwin,text="DeleteRec",font=24,fg="maroon",bg="silver",bd="20",command=DeleteRec)
            but4.place(x=690,y=550)
            win.destroy()
            siwin.destroy()
            messagebox.showinfo("SignIn","Login Successful!")
    userid=StringVar()
    password=StringVar()
    uid=userid.get()
    pas=password.get()
    ent2=Entry(siwin,font=("monotype corsiva",23),fg="maroon",bg="silver",width=37,bd=3,textvariable=userid)
    ent2.place(x=350,y=220)
    ent3=Entry(siwin,font=("monotype corsiva",23),fg="maroon",bg="silver",width=37,bd=3,textvariable=password,show="*")
    ent3.place(x=350,y=360)
    but1=Button(siwin,text="Sign In ",font=24,fg="maroon",bg="silver",bd="20",command=check_credential)
    but1.place(x=300,y=500)
    but2=Button(siwin,text=" Reset ",font=24,fg="maroon",bg="silver",bd="20",command=Reset)
    but2.place(x=500,y=500)
    but3=Button(siwin,text="  Exit   ",font=24,fg="maroon",bg="silver",bd="20",command=exit)
    but3.place(x=700,y=500)
    but4=Button(siwin,text="Sign Up ",font=24,fg="maroon",bg="silver",bd="10",command=SignUp)
    but4.place(x=890,y=62)
def exit():
    win.destroy()

win.iconbitmap("C:\\Users\\Anant\\Desktop\\logo.ico")
photof=Image.open("C:\\Users\\Anant\\Desktop\\hubnet.png")
rphoto=photof.resize((600,500))
photoff=ImageTk.PhotoImage(rphoto)
image=Label(win,image=photoff)
image.place(x=70,y=97)
photo1=PhotoImage(file="C:\\Users\\Anant\\Desktop\\hubnet.png")
img=Label(win,image=photo1)
label1=Label(win,text="\tWelcome To Hubnet Student Management System\t    ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
label1.place(x=2,y=3)
label2=Label(win,text="  Website Address: 'www.hubnettech.net'      Mob-No. : 8589848785   ",font=("monotype corsiva",28,"bold"),bg="silver",fg="maroon")
label2.place(x=2,y=647)
but1=Button(win,text="Sign Up",font=24,fg="maroon",bg="silver",bd="30",command=SignUp)
but1.place(x=750,y=150)
but2=Button(win,text="Sign In ",font=24,fg="maroon",bg="silver",bd="30",command=SignIn)
but2.place(x=750,y=300)
but3=Button(win,text="  Exit   ",font=24,fg="maroon",bg="silver",bd="30",command=exit)
but3.place(x=750,y=450)
win.mainloop()
