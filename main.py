from tkinter import *
from tkinter import messagebox, ttk
import pymysql
from datetime import datetime

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="#fa991c")

        title_label = Label(self.root, text="Employee Payroll Management System", bd=12, relief=GROOVE, font=("times new roman", 30, "bold"), bg="#032539", fg="#1c768f", anchor="center", padx=10)
        title_label.place(x=0, y=0, relwidth=1)

        # ------------Frame1-----------#
        # ----------Variables----------
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar() 
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_age = StringVar()
        self.var_experience = StringVar()
        self.var_gender = StringVar()
        self.var_pi = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()

        Frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="#fbf3f2")
        Frame1.place(x=8, y=70, width=1140, height=940)
        title2 = Label(Frame1, text="Employee Details", font=("times new roman", 20,), bg="#1c768f", fg="#032539", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        lbl_code = Label(Frame1, text="Employee Code", font=("times new roman", 20,), bg="#fbf3f2", fg="#032539").place(x=10, y=70)
        txt_code = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_emp_code, bg="#fbf3a1", fg="#032539").place(x=200, y=70, width=600, height=40)
        btn_search = Button(Frame1, text="Search", font=("times new roman", 20,), bg="#1c768f", fg="#032539", command=self.search).place(x=830, y=72.5, height=30)

        # --Row1
        lbl_designation = Label(Frame1, text="Designation", font=("times new roman", 20,), bg="#fbf3f2", fg="#032539").place(x=10, y=130)
        txt_designation = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_designation, bg="#fbf3a1", fg="#032539").place(x=200, y=138, width=300)

        lbl_doj = Label(Frame1, text="Date Of Joining", font=("times new roman", 20,), bg="#fbf3f2", fg="#032539").place(x=530, y=130)
        txt_doj = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_doj, bg="#fbf3a1", fg="#032539").place(x=750, y=138, width=300)

        # --Row2
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 20,), bg="#fbf3f2", fg="#032539").place(x=10, y=230)
        txt_name = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_name, bg="#fbf3a1", fg="#032539").place(x=200, y=230, width=300)

        lbl_dob = Label(Frame1, text="Date Of Birth", font=("times new roman", 20,), bg="#fbf3f2", fg="#032539").place(x=530, y=230)
        txt_dob = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_dob, bg="#fbf3a1", fg="#032539").place(x=750, y=230, width=300)

        # --Row4
        lbl_age = Label(Frame1, text="Age", font=("Times new Roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=330)
        txt_age = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_age, bg="#fbf3a1", fg="#032539").place(x=200, y=330, width=300)

        lbl_experience = Label(Frame1, text="Experience", font=("Times new Roman", 20), bg="#fbf3f2", fg="#032539").place(x=530, y=330)
        txt_experience = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_experience, bg="#fbf3a1", fg="#032539").place(x=750, y=330, width=300)

        # --Row5
        lbl_gender = Label(Frame1, text="Gender", font=("Times new Roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=430)
        txt_gender = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_gender, bg="#fbf3a1", fg="#032539").place(x=200, y=430, width=300)

        lbl_pf = Label(Frame1, text="Proof ID", font=("Times new Roman", 20), bg="#fbf3f2", fg="#032539").place(x=530, y=430)
        txt_pf = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_pi, bg="#fbf3a1", fg="#032539").place(x=750, y=430, width=300)

        # --Row6
        lbl_email = Label(Frame1, text="Email", font=("Times new Roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=530)
        txt_email = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_email, bg="#fbf3a1", fg="#032539").place(x=200, y=530, width=300)

        lbl_contact = Label(Frame1, text="Contact No:", font=("Times new Roman", 20), bg="#fbf3f2", fg="#032539").place(x=530, y=530)
        txt_contact = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_contact, bg="#fbf3a1", fg="#032539").place(x=750, y=530, width=300)

        # --Row7
        lbl_address = Label(Frame1, text="Address:", font=("Times new Roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=630)
        self.txt_address = Text(Frame1, font=("times new roman", 15), bg="#fbf3a1", fg="#032539")
        self.txt_address.place(x=200, y=630, width=800, height=200)

        # ==========Frame2============#
        # --------------Variables------
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_total_days = StringVar()
        self.var_absents = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()

        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="#fbf3f2")
        Frame2.place(x=1155, y=70, width=760, height=480)

        title2 = Label(Frame2, text="Employee Salary Details", font=("times new roman", 20), bg="#1c768f", fg="#032539", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        # --Row1
        lbl_month = Label(Frame2, text="Month:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=70)
        txt_month = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_month, bg="#fbf3a1", fg="#032539").place(x=100, y=70, width=100)

        lbl_year = Label(Frame2, text="Year:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=230, y=70)
        txt_year = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_year, bg="#fbf3a1", fg="#032539").place(x=310, y=70, width=100)

        lbl_salary = Label(Frame2, text="Salary:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=430, y=70)
        txt_salary = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_salary, bg="#fbf3a1", fg="#032539").place(x=520, y=70, width=100)

        # --Row2
        lbl_total_days = Label(Frame2, text="Total Days:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=135)
        txt_total_days = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_total_days, bg="#fbf3a1", fg="#032539").place(x=170, y=140, width=100)

        lbl_absents = Label(Frame2, text="Absents:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=300, y=135)
        txt_absents = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_absents, bg="#fbf3a1", fg="#032539").place(x=430, y=140, width=100)

        lbl_medical = Label(Frame2, text="Medical:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=190)
        txt_medical = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_medical, bg="#fbf3a1", fg="#032539").place(x=170, y=195, width=100)

        lbl_pf = Label(Frame2, text="P.F:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=300, y=190)
        txt_pf = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_pf, bg="#fbf3a1", fg="#032539").place(x=430, y=195, width=100)

        lbl_convence = Label(Frame2, text="Convence:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=10, y=250)
        txt_convence = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_convence, bg="#fbf3a1", fg="#032539").place(x=170, y=255, width=100)

        btn_calculate = Button(Frame2, text="Calculate", command=self.calculate, font=("times new roman", 20), bg="#1c768f", fg="#032539").place(x=10, y=350, height=30, width=120)

        lbl_net_salary = Label(Frame2, text="Net Salary:", font=("times new roman", 20), bg="#fbf3f2", fg="#032539").place(x=300, y=250)
        txt_net_salary = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_net_salary, bg="#fbf3a1", fg="#032539").place(x=450, y=255, width=100)

        btn_save = Button(Frame2, text="Save", font=("times new roman", 20), bg="#1c768f", fg="#032539", command=self.add).place(x=150, y=350, height=30, width=120)
        btn_update = Button(Frame2, text="Update", font=("times new roman", 20), bg="#1c768f", fg="#032539", command=self.update).place(x=290, y=350, height=30, width=120)
        btn_delete = Button(Frame2, text="Delete", font=("times new roman", 20), bg="#1c768f", fg="#032539", command=self.delete).place(x=430, y=350, height=30, width=120)
        btn_clear = Button(Frame2, text="Clear", font=("times new roman", 20), bg="#1c768f", fg="#032539", command=self.clear).place(x=570, y=350, height=30, width=120)

        # ===Frame3=====#
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="#fbf3f2")
        Frame3.place(x=1155, y=560, width=760, height=450)

        title3 = Label(Frame3, text="Salary Reciept", font=("times new roman", 20), bg="#1c768f", fg="#032539", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        scroll_y = Scrollbar(Frame3, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_recipt = Text(Frame3, font=("times new roman", 15), bg="#fbf3f2", fg="#032539", yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)

        # Adding Employee Table
        self.EmployeeTable = ttk.Treeview(self.root, columns=("emp_code", "name", "dob", "doj", "gender", "email", "contact", "designation", "pf", "experience", "age", "address", "salary"))
        self.EmployeeTable.place(x=8, y=1020, width=1900, height=200)
        self.EmployeeTable.heading("emp_code", text="Emp Code")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("dob", text="DOB")
        self.EmployeeTable.heading("doj", text="DOJ")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("designation", text="Designation")
        self.EmployeeTable.heading("pf", text="Proof ID")
        self.EmployeeTable.heading("experience", text="Experience")
        self.EmployeeTable.heading("age", text="Age")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")
        self.EmployeeTable["show"] = "headings"

        # Bind the treeview selection event
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

    def search(self):


        #------database connect------------
        con = pymysql.connect(host='localhost', user='root', password='1234', database='employeeinfo')
        cur = con.cursor()
        try:
            if self.var_emp_code.get() == "":
                messagebox.showerror("Error", "Employee code must be required")
            else:
                cur.execute("SELECT * FROM employees WHERE emp_code=%s", (self.var_emp_code.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee code, Try again")
                else:
                    self.var_emp_code.set(row[0])
                    self.var_designation.set(row[1])
                    self.var_name.set(row[2])
                    self.var_dob.set(row[3])
                    self.var_doj.set(row[4])
                    self.var_age.set(row[5])
                    self.var_experience.set(row[6])
                    self.var_gender.set(row[7])
                    self.var_pi.set(row[8])
                    self.var_email.set(row[9])
                    self.var_contact.set(row[10])

                    self.var_month.set(row[12])
                    self.var_year.set(row[13])
                    self.txt_address.delete('1.0', END)
                    self.txt_address.insert(END, row[11])
                    
                    self.var_salary.set(row[14])#--------------------------------------------------------------------
                    self.var_total_days.set(row[15])
                    self.var_absents.set(row[16])
                    self.var_medical.set(row[17])
                    self.var_pf.set(row[18])
                    self.var_convence.set(row[19])
                    self.var_net_salary.set(row[20])
                    self.receipt()

                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        con.close()

    def add(self):

        #----database connect----------
        con = pymysql.connect(host='localhost', user='root', password='1234', database='employeeinfo')
        cur = con.cursor()
        try:
            if self.var_emp_code.get() == "":
                messagebox.showerror("Error", "Employee code must be required")
            else:
                cur.execute("INSERT INTO employees (emp_code, designation, name, dob,  doj, age, experience, gender, pi, email, contact, address, month, year, salary , total_days , absents, medical, pf, convence, net_salary ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_emp_code.get(),
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_age.get(),
                    self.var_experience.get(),
                    self.var_gender.get(),
                    self.var_pi.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.txt_address.get('1.0', END),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_total_days.get(),
                    self.var_absents.get(),
                    self.var_medical.get(),
                    self.var_pf.get(),
                    self.var_convence.get(),

                    self.var_net_salary.get(),
                ))
                con.commit()
                messagebox.showinfo("Success", "Employee Added Successfully")
                self.clear()
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        con.close()

    def show(self):

        con = pymysql.connect(host='localhost', user='root', password='1234', database='employeeinfo')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        con.close()

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content['values']
        self.var_emp_code.set(row[0])
        self.var_designation.set(row[1])
        self.var_name.set(row[2])
        self.var_age.set(row[3])
        self.var_dob.set(row[4])
        self.var_doj.set(row[5])
        self.var_email.set(row[6])
        self.var_gender.set(row[7])
        self.var_contact.set(row[8])
        self.var_experience.set(row[9])
        self.var_pi.set(row[10])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[11])
        self.var_salary.set(row[12])
        self.var_year.set(row[13])
        self.txt_address.delete('1.0', END)
                    
        self.var_salary.set(row[14])#--------------------------------------------------------------------
        self.var_total_days.set(row[15])
        self.var_absents.set(row[16])
        self.var_medical.set(row[17])
        self.var_pf.set(row[18])
        self.var_convence.set(row[19])
        self.var_net_salary.set(row[20])




    def update(self):
        #------connect databse----------
        con = pymysql.connect(host='localhost', user='root', password='1234', database='employeeinfo')
        cur = con.cursor()
        try:
            if self.var_emp_code.get() == "":
                messagebox.showerror("Error", "Employee code must be required")
            else:
                cur.execute("UPDATE employees SET designation=%s, name=%s, dob=%s, doj=%s, age=%s, experience=%s, gender=%s, email=%s, contact=%s, address=%s, month=%s, year=%s, salary=%s, total_days=%s, absents=%s, medical=%s, pf=%s, convence=%s, net_salary=%s WHERE emp_code=%s", (
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_age.get(),
                    self.var_experience.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_pi.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.txt_address.get('1.0', END),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_total_days.get(),
                    self.var_absents.get(),
                    self.var_medical.get(),
                    self.var_pf.get(),
                    self.var_convence.get(),

                    self.var_net_salary.get(),
                    self.var_emp_code.get(),
                ))
                con.commit()
                messagebox.showinfo("Success", "Employee Updated Successfully")
                self.clear()
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        con.close()

    def delete(self):
        #----connect database----------
        con = pymysql.connect(host='localhost', user='root', password='1234', database='employeeinfo')
        cur = con.cursor()
        try:
            if self.var_emp_code.get() == "":
                messagebox.showerror("Error", "Employee code must be required")
            else:
                cur.execute("DELETE FROM employees WHERE emp_code=%s", (self.var_emp_code.get(),))
                con.commit()
                messagebox.showinfo("Success", "Employee Deleted Successfully")
                self.clear()
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        con.close()

    def clear(self):
        self.var_emp_code.set("")
        self.var_designation.set("")
        self.var_name.set("")
        self.var_age.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_experience.set("")
        self.var_pi.set("")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        
                    
                    
        self.var_month.set("")
        self.var_year.set("")
        
        self.var_total_days.set("")
        self.var_absents.set("")
        self.var_medical.set("")
        self.var_pf.set("")
        self.var_convence.set("")

        self.var_net_salary.set(""),
    
#------Function use for recipt-------------
    def receipt(self):
        self.txt_salary_recipt.delete('1.0', END)
        self.txt_salary_recipt.insert(END, "\tFAM\n")
        self.txt_salary_recipt.insert(END, f"\nMonth : {self.var_month.get()} Year : {self.var_year.get()}")
        self.txt_salary_recipt.insert(END, f"\n\nEmployee ID : {self.var_emp_code.get()}")
        self.txt_salary_recipt.insert(END, f"\nEmployee Name : {self.var_name.get()}")
        self.txt_salary_recipt.insert(END, f"\nDesignation : {self.var_designation.get()}")
        self.txt_salary_recipt.insert(END, f"\nSalary : {self.var_salary.get()}")
        self.txt_salary_recipt.insert(END, f"\nTotal Days : {self.var_total_days.get()}")
        self.txt_salary_recipt.insert(END, f"\nAbsents : {self.var_absents.get()}")
        self.txt_salary_recipt.insert(END, f"\nMedical : {self.var_medical.get()}")
        self.txt_salary_recipt.insert(END, f"\nP.F : {self.var_pf.get()}")
        self.txt_salary_recipt.insert(END, f"\nConvence : {self.var_convence.get()}")

        self.txt_salary_recipt.insert(END, f"\nNet Salary : {self.var_net_salary.get()}")
                    

    def calculate(self):
        try:
            if self.var_month.get() == "" or self.var_year.get() == "" or self.var_salary.get() == "" or self.var_total_days.get() == "" or self.var_absents.get() == "" or self.var_medical.get() == "" or self.var_pf.get() == "" or self.var_convence.get() == "":
                messagebox.showerror("Error", "All fields are required")
            else:
                # Salary Calculation
                salary_per_day = int(self.var_salary.get()) / int(self.var_total_days.get())
                salary = salary_per_day * (int(self.var_total_days.get()) - int(self.var_absents.get()))
                deduct = int(self.var_medical.get()) + int(self.var_pf.get()) + int(self.var_convence.get())
                net_salary = salary - deduct
                self.var_net_salary.set(str(round(net_salary, 2)))

                # Receipt
                self.txt_salary_recipt.delete('1.0', END)
                self.txt_salary_recipt.insert(END, "\tFAM\n")
                self.txt_salary_recipt.insert(END, f"\nMonth : {self.var_month.get()} Year : {self.var_year.get()}")
                self.txt_salary_recipt.insert(END, f"\n\nEmployee ID : {self.var_emp_code.get()}")
                self.txt_salary_recipt.insert(END, f"\nEmployee Name : {self.var_name.get()}")
                self.txt_salary_recipt.insert(END, f"\nDesignation : {self.var_designation.get()}")
                self.txt_salary_recipt.insert(END, f"\nSalary : {self.var_salary.get()}")
                self.txt_salary_recipt.insert(END, f"\nTotal Days : {self.var_total_days.get()}")
                self.txt_salary_recipt.insert(END, f"\nAbsents : {self.var_absents.get()}")
                self.txt_salary_recipt.insert(END, f"\nMedical : {self.var_medical.get()}")
                self.txt_salary_recipt.insert(END, f"\nP.F : {self.var_pf.get()}")
                self.txt_salary_recipt.insert(END, f"\nConvence : {self.var_convence.get()}")

                self.txt_salary_recipt.insert(END, f"\nNet Salary : {self.var_net_salary.get()}")
                

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
