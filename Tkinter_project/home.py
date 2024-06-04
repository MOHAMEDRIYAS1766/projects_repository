from tkinter import *
import sqlite3 as sql
import tkinter.messagebox as msg

root = Tk()
root.title('LPG GAS MANAGEMENT-Home')
root.geometry('900x600')
bg_image = PhotoImage(file='ave.png')

bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

TopHeadingFrame = Frame(root, width=700, bd=1)
TopHeadingFrame.pack(side=TOP)
Heading_label = Label(TopHeadingFrame, text='LPG Gas Booking Management System-Home', fg='white', bg='red', font=('Helvetica', 15))
Heading_label.grid(row=0, column=0, padx=10, pady=10)

MidFrame=Frame(root,width=900,bd=1)
MidFrame=LabelFrame(root,
	bg='lightgreen',highlightbackground='blue',highlightthickness=10)
MidFrame.pack(side=TOP)

def Logout():
    root.destroy()
    import user_login
def add():
    root.destroy()
    import add_booking
def view():
    root.destroy()
    import search_booking_using_no

def delete():
    root.destroy()
    import delete_booking
AddButton = Button(MidFrame, text='Add Booking', fg='purple', bg='lightblue', font=('Helvetica', 15),command=add,cursor='hand2')
AddButton.grid(row=0, column=1, padx=10, pady=10)

ViewButton = Button(MidFrame, text='View Booking details', fg='purple', bg='lightblue', font=('Helvetica', 15),command=view,cursor='hand2')
ViewButton.grid(row=1, column=1, padx=10, pady=10)

DeleteButton = Button(MidFrame, text='Delete Booking', fg='purple', bg='lightblue', font=('Helvetica', 15),command=delete,cursor='hand2')
DeleteButton.grid(row=3, column=1, padx=10, pady=10)

EndFrame = Frame(root, width=700, bd=1)
EndFrame=LabelFrame(root,
	bg='lightgreen',highlightbackground='blue')
EndFrame.pack(side=TOP)
LogoutButton = Button(EndFrame, text='Logout', fg='white', bg='purple', font=('Helvetica', 15),command=Logout,cursor='hand1')
LogoutButton.grid(row=0, column=0, padx=10, pady=10)
root.mainloop()
