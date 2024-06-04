from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg
root=Tk()
root.geometry('900x900')
root.title('View Details About Customer ')
bg=PhotoImage(file='ave.png')
bg_img=Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)
top_frame=Frame(root,width=900,bd=1)
top_frame.pack(side=TOP)
MidFrame=Frame(root,width=900,bd=1)
MidFrame=LabelFrame(root,
	bg='lightgreen',highlightbackground='blue',highlightthickness=10)
MidFrame.pack(side=TOP)

titlename=Label(top_frame,text='View Details About Customer',bg='red',fg='white',font=('Helvetica', 18))
titlename.grid(row=0,column=0,padx=10,pady=10)

def Logout():
    root.destroy()
    import user_login


def search_user():
    root.destroy()
    import search_user

def search_booking():
    root.destroy()
    import search_booking

def delete_user():
    root.destroy()
    import delete_user

def delete_booking():
    root.destroy()
    import delete_booking
    

def customerdetail():
    root.destroy()
    import view_user_tbl


def customerbooking():
    root.destroy()
    import view_booking_tbl
    
    


customerdetail_btn=Button(MidFrame,text='View Customer Details',bg='lightblue',fg='purple',font=('Helvetica', 15),command=customerdetail,cursor="hand2")
customerdetail_btn.grid(row=2,column=0,padx=10,pady=10)

customerbooking_btn=Button(MidFrame,text='View Customer Booking Details',bg='lightblue',fg='purple',font=('Helvetica', 15),command=customerbooking,cursor="hand2")
customerbooking_btn.grid(row=2,column=1,padx=10,pady=10)

search1_btn=Button(MidFrame,text='Search  Customer  Details',bg='lightblue',fg='purple',font=('Helvetica', 15),command=search_user,cursor="hand2")
search1_btn.grid(row=3,column=0,padx=10,pady=10)

search2_btn=Button(MidFrame,text='Search  Customer Booking Details',bg='lightblue',fg='purple',font=('Helvetica', 15),command=search_booking,cursor="hand2")
search2_btn.grid(row=3,column=1,padx=10,pady=10)

delete_btn=Button(MidFrame,text='Delete Customer  Details',bg='lightblue',fg='purple',font=('Helvetica', 15),command=delete_user,cursor="hand2")
delete_btn.grid(row=4,column=0,padx=10,pady=10)

delete_btn=Button(MidFrame,text='Delete Customer Booking Details',bg='lightblue',fg='purple',font=('Helvetica', 15),command=delete_booking,cursor="hand2")
delete_btn.grid(row=4,column=1,padx=10,pady=10)



LogoutButton = Button(MidFrame, text='Logout', fg='white', bg='purple', font=('Helvetica', 15),command=Logout,cursor="hand1")
LogoutButton.grid(row=5, column=0, padx=10, pady=10)



