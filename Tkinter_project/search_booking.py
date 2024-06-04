from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg
import tkinter.ttk as ttk
root=Tk()
root.geometry('900x900')
root.title('Search booking details')
bg=PhotoImage(file='ave.png')
bg_img=Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)
top_frame=Frame(root,width=900,bd=1)
top_frame.pack(side=TOP)
titlename=Label(top_frame,text='SEARCH PAGE',bg='red',fg='white',font=('Helvetica', 18))
titlename.grid(row=0,column=0,padx=10,pady=10)


name=StringVar()
name.set('')

miframe=Frame(root,width=900,bd=1)
miframe=LabelFrame(root,
	bg='lightgreen',highlightbackground='blue',
highlightthickness=10)
miframe.pack(side=TOP)

Name=Label(miframe,text='Name',bg='orange',fg='white',font=('Helvetica', 15))
Name.grid(row=0,column=0,padx=10,pady=10)

nameE=Entry(miframe,textvariable=name)
nameE.grid(row=0,column=1,padx=10,pady=10)

mid_frame=Frame(root,width=900,bd=1)
mid_frame=LabelFrame(root,
	bg='lightgreen',
highlightthickness=10)
mid_frame.pack(side=TOP)


view=ttk.Treeview(mid_frame,columns=('name','number','brand','year','month','amount'),height=200,selectmode = 'extended')
view.heading('name',text='NAME',anchor=W)
view.heading('number',text='NUMBER',anchor=W)
view.heading('brand',text='BRAND',anchor=W)
view.heading('year',text='YEAR',anchor=W)
view.heading('month',text='MONTH',anchor=W)
view.heading('amount',text='AMOUNT',anchor=W)


view.pack()
view.column('#0',stretch = NO,width = 50,minwidth=0)
view.column('#1',stretch = NO,width = 50,minwidth=0)
view.column('#2',stretch = NO,width = 150,minwidth=0)
view.column('#3',stretch = NO,width = 150,minwidth=0)
view.column('#4',stretch = NO,width = 100,minwidth=0)
view.column('#5',stretch = NO,width = 100,minwidth=0)
view.column('#6',stretch = NO,width = 100,minwidth=0)

def back():
    root.destroy()
    import adminpage




def search():
    conn=sql.connect('use.db')
    cursor=conn.cursor()
    cursor.execute(""" select * from 'booking_tbl' where name=?""",(name.get(),))
    conn.commit()
    data=list(cursor.fetchall())
    for i in data:
        view.insert('','end',value=(i))

    
search_btn=Button(miframe,text='SEARCH',bg='lightblue',fg='purple',font=('Helvetica', 15),command=search,cursor="hand2")
search_btn.grid(row=4,column=1,padx=10,pady=10)

back_btn=Button(miframe,text='Back',bg='lightblue',fg='purple',font=('Helvetica', 15),command=back,cursor="hand2")
back_btn.grid(row=4,column=0,padx=10,pady=10)

