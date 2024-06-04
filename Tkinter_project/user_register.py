from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg
root=Tk()
root.geometry('900x900')
root.title('register here')
bg=PhotoImage(file='ave.png')
bg_img=Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)
top_frame=Frame(root,width=900,bd=1)
top_frame.pack(side=TOP)
name=StringVar()
email=StringVar()
password=StringVar()
number=IntVar()

name.set('')
email.set('')
password.set('')
number.set('')
conn=sql.connect('use.db')
cursor=conn.cursor()
cursor.execute(""" create table  if not exists 'newuser' (id INTEGER PRIMARY KEY,name text,email text,password text,number int)""")
conn.commit()

titlename=Label(top_frame,text='REGISTER PAGE',bg='red',fg='white',font=('Helvetica', 18))
titlename.grid(row=0,column=0,padx=10,pady=10)

mid_frame=Frame(root,width=900,bd=1)
mid_frame=LabelFrame(root,text="Register Here",
	bg='lightgreen',highlightbackground='blue',highlightcolor='yellow',
highlightthickness=10)
mid_frame.pack(side=TOP)

Name=Label(mid_frame,text='Name',bg='orange',fg='white',font=('Helvetica', 15))
Name.grid(row=0,column=0,padx=10,pady=10)
Email=Label(mid_frame,text='Email',bg='orange',fg='white',font=('Helvetica', 15))
Email.grid(row=1,column=0,padx=10,pady=10)
Password=Label(mid_frame,text='Password',bg='orange',fg='white',font=('Helvetica', 15))
Password.grid(row=2,column=0,padx=10,pady=10)
Number=Label(mid_frame,text='Mobile Number',bg='orange',fg='white',font=('Helvetica', 15))
Number.grid(row=3,column=0,padx=10,pady=10)
alreadyregistrer=Label(mid_frame,text='Already have an Accont',bg='orange',fg='white',font=('Helvetica', 15))
alreadyregistrer.grid(row=5,column=0,padx=10,pady=10)

nameE=Entry(mid_frame,textvariable=name)
nameE.grid(row=0,column=1,padx=10,pady=10)
emailE=Entry(mid_frame,textvariable=email)
emailE.grid(row=1,column=1,padx=10,pady=10)
passwordE=Entry(mid_frame,textvariable=password)
passwordE.grid(row=2,column=1,padx=10,pady=10)
numberE=Entry(mid_frame,textvariable=number)
numberE.grid(row=3,column=1,padx=10,pady=10)


def register():
    conn=sql.connect('use.db')
    cursor=conn.cursor()
    cursor.execute(""" insert into 'newuser' (name,email,password,number) values(?,?,?,?)""",
                   (str(name.get()),str(email.get()),str(password.get()),str(number.get())))
    conn.commit()
    if  cursor.rowcount>0:
        msg.showinfo('register information','register successfully added',icon='info')
        root.destroy()
        import user_login
    else:
        msg.showinfo('register information','register is not added',icon='warning')

def login():
        root.destroy()
        import user_login
    

regbtn=Button(mid_frame,text='Rregister',bg='lightblue',fg='purple',font=('Helvetica', 15),command=register,cursor='hand2')
regbtn.grid(row=4,column=1,padx=10,pady=10)
loginbtn=Button(mid_frame,text='Login',bg='lightblue',fg='purple',font=('Helvetica', 15),command=login,cursor='hand1')
loginbtn.grid(row=5,column=1,padx=10,pady=10)

