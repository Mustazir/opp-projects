from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def clear():
    usernameEntry.delete(0,END)
    emaiilEntry.delete(0,END)
    employeeIdEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    check.set(0)
    signup_window.destroy()
    import login


def login_page():
    signup_window.destroy()
    import login

#----------------Database--------------

def connect_database():
    if emaiilEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()==''or employeeIdEntry.get()=='':
        messagebox.showerror('Error','All fields are Required')

    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()== 0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:

#--------------Database Connect--------------
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()

        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

#------------Create cell in database for user information----------
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='Use Userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,username varchar(100), email varchar(50),employeeid varchar(5),password varchar(20))'
            mycursor.execute(query)
        
        except:
            mycursor.execute('use userdata')

        query='insert into data(username,email,employeeid,password) values(%s,%s,%s,%s)'
        mycursor.execute(query,(usernameEntry.get(),emaiilEntry.get(),employeeIdEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Registration is Successful')
    clear()
    


        


    





signup_window=Tk()
signup_window.geometry('990x660+50+50')
signup_window.resizable(0,0)
signup_window.title('Sign Up Page')
bgimage=ImageTk.PhotoImage(file="sign.png")
bgLabel=Label(signup_window,image=bgimage)
bgLabel.place(x=0,y=0)

frame=Frame(signup_window)
frame.place(x=434,y=110)



heading=Label(frame,text='Create An Account',font=('Consolas',20,'bold'),bg='cyan')
heading.grid(row=1,column=1)



#username
usernameLabel=Label(signup_window,text='Username',font=('Consolas',17,'bold'),fg='Black',bg="white")
usernameLabel.place(x=230,y=170)

usernameEntry=Entry(signup_window,width=25,font=('Consolas',20,'bold'),bd=0,fg='#277dff')
usernameEntry.place(x=362,y=170)

#email
emailLabel=Label(signup_window,text='Email',font=('Consolas',17,'bold'),fg='Black',bg="white")
emailLabel.place(x=230,y=235)

emaiilEntry=Entry(signup_window,width=25,font=('Consolas',20,'bold'),bd=0,fg='#277dff')
emaiilEntry.place(x=362,y=235)

#employee id
employeeIdLabel=Label(signup_window,text='Id',font=('Consolas',17,'bold'),fg='Black',bg="white")
employeeIdLabel.place(x=230,y=300)

employeeIdEntry=Entry(signup_window,width=25,font=('Consolas',20,'bold'),bd=0,fg='#277dff')
employeeIdEntry.place(x=362,y=305)

#password

passwordLabel=Label(signup_window,text='Password',font=('Consolas',17,'bold'),fg='Black',bg="white")
passwordLabel.place(x=230,y=370)

passwordEntry=Entry(signup_window,width=25,font=('Consolas',20,'bold'),bd=0,fg='#277dff')
passwordEntry.place(x=362,y=370)

confirmpasswordLabel=Label(signup_window,text='Con.Pass',font=('Consolas',17,'bold'),fg='Black',bg="white")
confirmpasswordLabel.place(x=230,y=440)

confirmpasswordEntry=Entry(signup_window,width=25,font=('Consolas',20,'bold'),bd=0,fg='#277dff')
confirmpasswordEntry.place(x=362,y=440)


check=IntVar()
termsandconditions=Checkbutton(signup_window,text='I agree to the Terms & Conditions',font=('Consolas',7,'bold'),fg='Black',bg="white",cursor='hand2',variable=check)
termsandconditions.place(x=360,y=482)

signupButton=Button(signup_window,text="SignUp",font=("Open sans",10,'bold'),fg="white",bg='#277dff',cursor='hand2',bd=0,width=30,command=connect_database)
signupButton.place(x=425,y=510)                     


haveaccount=Label(signup_window,text='already HAve account?',font=('Consolas',7,'bold'),fg='Black',bg="white")
haveaccount.place(x=360,y=543)

loginButton=Button(signup_window,text='Login',bd=0,bg='white',activebackground='white',cursor='hand2',
                    font=('Consolas',10,'bold'),fg='red',command=login_page)

loginButton.place(x=479,y=540)

signup_window.mainloop()