from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg
root=Tk()
root.geometry('900x900')
root.title('Booking LPG')
bg=PhotoImage(file='ave.png')
bg_img=Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)
top_frame=Frame(root,width=900,bd=1)
top_frame.pack(side=TOP)
name=StringVar()
number=IntVar()
Brand=StringVar()
year=StringVar()
month=StringVar()
amount=IntVar()


name.set('')
number.set('')
Brand.set('')
year.set('')
month.set('')
amount.set('')

conn=sql.connect('use.db')
cursor=conn.cursor()
cursor.execute(""" create table  if not exists 'booking_tbl' (name text,number int,brand text,year text,month text,amount int)""")
conn.commit()

titlename=Label(top_frame,text='BOOKING PAGE',bg='red',fg='white',font=('Helvetica', 18))
titlename.grid(row=0,column=0,padx=10,pady=10)

mid_frame=Frame(root,width=900,bd=1)
mid_frame=LabelFrame(root,
	bg='lightgreen',highlightbackground='blue',highlightthickness=10)
mid_frame.pack(side=TOP)

Name=Label(mid_frame,text='Name',bg='orange',fg='white',font=('Helvetica', 15))
Name.grid(row=0,column=0,padx=10,pady=10)
Number=Label(mid_frame,text='Mobile Number',bg='orange',fg='white',font=('Helvetica', 15))
Number.grid(row=1,column=0,padx=10,pady=10)
brand=Label(mid_frame,text='Brand',bg='orange',fg='white',font=('Helvetica', 15))
brand.grid(row=2,column=0,padx=10,pady=10)
Year=Label(mid_frame,text='Year',bg='orange',fg='white',font=('Helvetica', 15))
Year.grid(row=3,column=0,padx=10,pady=10)
Month=Label(mid_frame,text='Month',bg='orange',fg='white',font=('Helvetica', 15))
Month.grid(row=4,column=0,padx=10,pady=10)
Amount=Label(mid_frame,text='Amount',bg='orange',fg='white',font=('Helvetica', 15))
Amount.grid(row=5,column=0,padx=10,pady=10)



nameE=Entry(mid_frame,textvariable=name)
nameE.grid(row=0,column=1,padx=10,pady=10)
numberE=Entry(mid_frame,textvariable=number)
numberE.grid(row=1,column=1,padx=10,pady=10)
brandE=Entry(mid_frame,textvariable=Brand)
brandE.grid(row=2,column=1,padx=10,pady=10)
yearE=Entry(mid_frame,textvariable=year)
yearE.grid(row=3,column=1,padx=10,pady=10)
monthE=Entry(mid_frame,textvariable=month)
monthE.grid(row=4,column=1,padx=10,pady=10)
amountE=Entry(mid_frame,textvariable=amount)
amountE.grid(row=5,column=1,padx=10,pady=10)

def back():
    root.destroy()
    import home

def register():
    conn=sql.connect('use.db')
    cursor=conn.cursor()
    cursor.execute(""" insert into 'booking_tbl' (name,number,brand,year,month,amount) values(?,?,?,?,?,?)""",
                   (str(name.get()),str(number.get()),str(Brand.get()),str(year.get()),str(month.get()),str(amount.get())))
    conn.commit()
    if  cursor.rowcount>0:
        msg.showinfo('booking information','booking successfully added',icon='info')
    else:
        msg.showinfo('booking information','booking is not added',icon='warning')
    

regbtn=Button(mid_frame,text='Booking',bg='lightblue',fg='purple',font=('Helvetica', 15),command=register,cursor='hand2')
regbtn.grid(row=6,column=1,padx=10,pady=10)
bacbtn=Button(mid_frame,text='Back',bg='lightblue',fg='purple',font=('Helvetica', 15),command=back,cursor='hand2')
bacbtn.grid(row=6,column=0,padx=10,pady=10)

