from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg
import tkinter.ttk as ttk
root=Tk()
root.geometry('900x900')
root.title('view user details')
bg=PhotoImage(file='ave.png')
bg_img=Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)
top_frame=Frame(root,width=900,bd=1)
top_frame.pack(side=TOP)
titlename=Label(top_frame,text='VIEW PAGE',bg='red',fg='white',font=('Helvetica', 18))
titlename.grid(row=0,column=0,padx=10,pady=10)

mid_frame=Frame(root,width=900,bd=1)
mid_frame=LabelFrame(root,
	bg='lightgreen',
highlightthickness=10)
mid_frame.pack(side=TOP)

view=ttk.Treeview(mid_frame,columns=('id','name','email','password','number'),height=200,selectmode = 'extended')
view.heading('id',text='ID',anchor=W)
view.heading('name',text='NAME',anchor=W)
view.heading('email',text='EMAIL',anchor=W)
view.heading('password',text='PASSWORD',anchor=W)
view.heading('number',text='NUMBER',anchor=W)

view.pack()
view.column('#0',stretch = NO,width = 50,minwidth=0)
view.column('#1',stretch = NO,width = 50,minwidth=0)
view.column('#2',stretch = NO,width = 150,minwidth=0)
view.column('#3',stretch = NO,width = 150,minwidth=0)
view.column('#4',stretch = NO,width = 100,minwidth=0)
view.column('#5',stretch = NO,width = 100,minwidth=0)

def back():
    root.destroy()
    import adminpage

conn=sql.connect('use.db')
cursor=conn.cursor()
cursor.execute(""" select * from 'newuser'""")
conn.commit()
data=list(cursor.fetchall())
for i in data:
    view.insert('','end',value=(i))


bacbtn=Button(top_frame,text='Back',bg='lightblue',fg='purple',font=('Helvetica', 15),command=back,cursor="hand2")
bacbtn.grid(row=0,column=4,padx=10,pady=10)

