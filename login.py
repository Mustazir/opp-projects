from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#--------All Fiunction-------------

def clear():
    usernameEntry.delete(0,END)
    
    passwordEntry.delete(0,END)
    

    login_window.destroy()
    import main

def login_page():
    login_window.destroy()
    import main


def login_usr():
    if usernameEntry.get()=='' or passwordEntry.get()=='':

        messagebox.showerror('Error','All Fields Are Required')

    else:
    #-----------Database Connect-----------
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='Use Userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()

        if row==None:
            messagebox.showerror('Error','Invalid username or password')

        else:
            messagebox.showinfo('Success','Login is Successful')
        clear()


        

def signup_page():
    login_window.destroy()
    import signup






def hide():
    openeye.config(file="hide.png")
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file="show.png")
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


#Gui part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgimage=ImageTk.PhotoImage(file="bg.png")

bgLabel=Label(login_window,image=bgimage)
bgLabel.place(x=0,y=0)

usernameEntry=Entry(login_window,width=25,font=('Consolas',20,'bold'),bd=0,fg='#277dff')
usernameEntry.place(x=313,y=273)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

passwordEntry=Entry(login_window,width=25,font=('Consolas',20,'bold'),bd=0,fg='#277dff')
passwordEntry.place(x=313,y=375)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)

openeye=PhotoImage(file='show.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=678,y=373)



loginButton=Button(login_window,text="Login",font=("Open sans",15,'bold'),fg="white",bg='#277dff',cursor='hand2',bd=0,width=30,command=login_usr)
loginButton.place(x=315,y=450)


signupButton=Button(login_window,text='Sign UP',bd=0,bg='white',activebackground='white',cursor='hand2',
                    font=('Consolas',15,'bold'),fg='red',command=signup_page)
signupButton.place(x=457,y=500)
login_window.mainloop()