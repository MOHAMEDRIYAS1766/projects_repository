from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg
import tkinter.ttk as ttk
root=Tk()
root.geometry('900x900')
root.title('Delete booking detail ')
bg=PhotoImage(file='ave.png')
bg_img=Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)
top_frame=Frame(root,width=900,bd=1)
top_frame.pack(side=TOP)
titlename=Label(top_frame,text='DELETE PAGE',bg='red',fg='white',font=('Helvetica', 18))
titlename.grid(row=0,column=0,padx=10,pady=10)

name=StringVar()
name.set('')

mid_frame=Frame(root,width=900,bd=1)
mid_frame=LabelFrame(root,
	bg='lightgreen',highlightbackground='blue',highlightthickness=10)
mid_frame.pack(side=TOP)

Name=Label(mid_frame,text='Name',bg='orange',fg='white',font=('Helvetica', 15))
Name.grid(row=0,column=0,padx=10,pady=10)

nameE=Entry(mid_frame,textvariable=name)
nameE.grid(row=0,column=1,padx=10,pady=10)

def back():
    root.destroy()
    import adminpage

def delete():
    conn=sql.connect('use.db')
    cursor=conn.cursor()
    cursor.execute(""" delete from 'booking_tbl' where name=?""",(name.get(),))
    
    conn.commit()
delbtn=Button(mid_frame,text='DELETE',bg='lightblue',fg='purple',font=('Helvetica', 15),command=delete,cursor="hand2")
delbtn.grid(row=4,column=1,padx=10,pady=10)
bacbtn=Button(mid_frame,text='Back',bg='lightblue',fg='purple',font=('Helvetica', 15),command=back,cursor="hand2")
bacbtn.grid(row=4,column=0,padx=10,pady=10)

