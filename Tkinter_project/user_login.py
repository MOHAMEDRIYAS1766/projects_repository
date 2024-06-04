from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg
root=Tk()
root.geometry('900x900')
root.title('login here')
bg=PhotoImage(file='ave.png')
bg_img=Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)
top_frame=Frame(root,width=900,bd=1)

top_frame.pack(side=TOP)

name=StringVar()
password=StringVar()

name.set('')
password.set('')

titlename=Label(top_frame,text='LOGIN PAGE',bg='red',fg='white',font=('Helvetica', 18))
titlename.grid(row=0,column=0,padx=10,pady=10)

mid_frame=Frame(root,width=900,bd=1)
mid_frame=LabelFrame(root,text="Login Here",
	bg='lightgreen',highlightbackground='blue',
highlightthickness=10)
mid_frame.pack(side=TOP)

Name=Label(mid_frame,text='Name',bg='orange',fg='white',font=('Helvetica', 15))
Name.grid(row=0,column=0,padx=10,pady=10)

Password=Label(mid_frame,text='Password',bg='orange',fg='white',font=('Helvetica', 15))
Password.grid(row=2,column=0,padx=10,pady=10)

nameE=Entry(mid_frame,textvariable=name)
nameE.grid(row=0,column=1,padx=10,pady=10)

passwordE=Entry(mid_frame,textvariable=password)
passwordE.grid(row=2,column=1,padx=10,pady=10)
def login():
    conn=sql.connect('use.db')
    cursor=conn.cursor()
    cursor.execute(""" select * from 'newuser' where name=?and password=?""",
                   (str(name.get()),str(password.get())))
    conn.commit()
    data=list(cursor.fetchall())
    if  len(data)>0:
        if data[0][1]=='sai' and data[0][3]:
            msg.showinfo('login information','login successfully ',icon='info')
            root.destroy()
            import adminpage
        else:
            msg.showinfo('login information','login successfully ',icon='info')
            root.destroy()
            import home
    else:
        msg.showinfo('login information','login failed',icon='warning')
    



loginbtn=Button(mid_frame,text='Login',bg='lightblue',fg='purple',font=('Helvetica', 15),command=login,cursor='hand2')
loginbtn.grid(row=4,column=1,padx=10,pady=10)
