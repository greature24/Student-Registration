import tkinter as tk

from tkinter import ttk, messagebox

import sqlite3


def register_user():
    username_info = username.get()
    password_info = password.get()
    try:
        con = sqlite3.connect("login.db")
        con.execute(" CREATE TABLE IF NOT EXISTS login ( email TEXT PRIMARY KEY UNIQUE, password TEXT);")
        con.execute(" INSERT INTO login VALUES(\"" + username_info + "\",\"" + password_info + "\")")
        con.commit()
    except AttributeError:
        messagebox.showinfo("Invalid","Email already exist. Please try another username!!")
    #print(" CREATE TABLE IF NOT EXISTS login ( username TEXT PRIMARY KEY , password TEXT);")
    #print(" INSERT INTO login VALUES(\"" + username_info + "\",\"" + password_info + "\")")
    screen1.destroy()
    messagebox.showinfo("Success","Successfully Registered")


def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,tk.END)
    password_entry1.delete(0,tk.END)
    connect = sqlite3.connect("login.db")
    cursor = connect.execute("SELECT * FROM login WHERE email = ? AND password = ?",[username1,password1])
    results = cursor.fetchall()
    if results:
        screen2.destroy()
        login_page()
    else:
        messagebox.showinfo("Invalid","Invalid Email/Password. Try Again!!!")




def login():
    global screen2
    firstwindow.destroy()
    screen2 = tk.Tk()
    screen2.geometry("300x250")
    screen2.title("LOGIN Details")
    tk.Label(screen2, text="Enter LOGIN Details below").pack()
    tk.Label(screen2, text="").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    tk.Label(screen2, text="Username").pack()
    username_entry1 = tk.Entry(screen2,textvariable = username_verify)
    username_entry1.pack()
    tk.Label(screen2, text="").pack()
    tk.Label(screen2, text="Password").pack()
    password_entry1 = tk.Entry(screen2,textvariable = password_verify)
    password_entry1.pack()
    tk.Label(screen2, text="").pack()
    tk.Button(screen2,text = "Login",width=10,height=1,cursor = "hand2", command = login_verify).pack()




def register():
    global screen1
    screen1 = tk.Toplevel()
    screen1.title("Registration")
    screen1.geometry("300x250")

    global username
    global password

    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(screen1,text="Enter your details below").pack()
    tk.Label(screen1,text="").pack()
    tk.Label(screen1,text="Username").pack()
    username_entry = tk.Entry(screen1,textvariable= username)
    username_entry.pack()
    tk.Label(screen1,text="Password").pack()
    password_entry = tk.Entry(screen1, textvariable=password)
    password_entry.pack()
    tk.Label(screen1,text="").pack()
    tk.Button(screen1,text="Register",width=10,height=1,command = register_user, cursor="hand2").pack()


def mainwindow():
    global firstwindow
    firstwindow = tk.Tk()
    firstwindow.geometry("300x250")
    firstwindow.title("JEE MAINS Registration")
    tk.Label(text = "JEE MAINS Registration",width=300,height=5,font=("Times new roman",13)).pack()
    tk.Label(text="").pack()
    tk.Button(text="LOGIN", height=2, width=30,cursor = "hand2",command = login).pack()
    tk.Label(text="").pack()
    tk.Button(text="REGISTER", height=2, width=30,cursor = "hand2", command= register).pack()
    firstwindow.mainloop()



def login_page():
    global root

    root = tk.Tk()
    root.title("JEE MAINS Registration")

    connection = sqlite3.connect('login.db')

    global TABLE_NAME, STUDENT_NAME, FATHER_NAME, MOTHER_NAME, AADHAR_NO, STUDENT_ADDRESS, STUDENT_PHONE,EMAIL,GENDER,CLASS12,CLASS10

    TABLE_NAME = "management_table"
    STUDENT_NAME = "student_name"
    FATHER_NAME = "father_name"
    EMAIL = "email"
    GENDER = "gender"
    CLASS12 = "class12"
    CLASS10 = "class10"
    MOTHER_NAME = "mother_name"
    AADHAR_NO = "aadhar_no"
    STUDENT_ADDRESS = "student_address"
    STUDENT_PHONE = "student_phone"


    connection.execute("  ")


    appLabel = tk.Label(root, text="JEE MAINS Registration", fg="#06a099", width=35)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))


    nameLabel = tk.Label(root, text="Candidate's Name :", width=40, anchor='w',
                         font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),pady=(30, 0))

    fatherLabel = tk.Label(root, text="Father Name :", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

    motherLabel = tk.Label(root, text="Mother Name :", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))

    aadharLabel = tk.Label(root, text="Aadhar Number :", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

    genderLabel = tk.Label(root, text="Gender :", width=40, anchor='w',
                           font=("Sylfaen",12)).grid(row=5, column=0, padx=(10,0))

    class12Label = tk.Label(root, text="Percentage in Class 12 :", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))

    class10Label = tk.Label(root, text="Percentage in Class 10 :", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=7, column=0, padx=(10, 0))

    phoneLabel = tk.Label(root, text="Mobile Number :", width=40, anchor='w',
                          font=("Sylfaen", 12)).grid(row=8, column=0, padx=(10,0))

    addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=9, column=0, padx=(10,0))

    global nameEntry, fatherEntry, motherEntry, aadharEntry, genderEntry, class12Entry, class10Entry, phoneEntry, addressEntry

    nameEntry = tk.Entry(root, width = 30)
    fatherEntry = tk.Entry(root, width = 30)
    motherEntry = tk.Entry(root, width = 30)
    aadharEntry = tk.Entry(root, width = 30)
    genderEntry = ttk.Combobox(root, width = 27, values= ("Male","Female","Transgender","Others"))
    #DOBEntry = tk.Entry(root,width=30)
    class12Entry = tk.Entry(root, width = 30)
    class10Entry = tk.Entry(root, width=30)
    phoneEntry = tk.Entry(root, width = 30)
    addressEntry = tk.Entry(root, width = 30)

    nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
    fatherEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
    motherEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
    aadharEntry.grid(row=4, column=1, padx=(0,10), pady = 20)
    genderEntry.grid(row=5, column=1, padx=(0,10), pady = 20)
    #DOBEntry.grid(row=6, column=1, padx=(0,10), pady = 20)
    class12Entry.grid(row=6, column=1, padx=(0,10), pady = 20)
    class10Entry.grid(row=7, column=1, padx=(0, 10), pady=20)
    phoneEntry.grid(row=8, column=1, padx=(0,10), pady = 20)
    addressEntry.grid(row=9, column=1, padx=(0,10), pady = 20)

    button = tk.Button(root, text="Take input", command=lambda: takeNameInput(), cursor = "hand2")
    button.grid(row=11, column=0, pady=30)

    displayButton = tk.Button(root, text="Display result", command=lambda: destroyRootWindow(), cursor = "hand2")
    displayButton.grid(row=11, column=1)

    root.mainloop()
    connection.close()

class Student:
    email = ""
    studentName = ""
    fathername = ""
    mothername = ""
    aadharno = ""
    gender = ""
    class12 = ""
    class10 = ""
    phoneNumber = ""
    address = ""

    def __init__(self, meail, studentName, fathername,mothername,aadharno,gender,class12,class10, phoneNumber, address):
        self.email = email
        self.studentName = studentName
        self.fathername = fathername
        self.mothername = mothername
        self.aadharno = aadharno
        self.gender = gender
        self.class12 = class12
        self.class10 = class10
        self.phoneNumber = phoneNumber
        self.address = address


def takeNameInput():
    global list
    email = username1
    name = nameEntry.get()
    nameEntry.delete(0, tk.END)
    fathername = fatherEntry.get()
    fatherEntry.delete(0, tk.END)
    mothername = motherEntry.get()
    motherEntry.delete(0,tk.END)
    aadharno = aadharEntry.get()
    aadharEntry.delete(0,tk.END)
    gender = genderEntry.get()
    genderEntry.delete(0,tk.END)
    class12 = class12Entry.get()
    class12Entry.delete(0,tk.END)
    class10 = class10Entry.get()
    class10Entry.delete(0,tk.END)
    phone = phoneEntry.get()
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)
    con = sqlite3.connect("login.db")
    con.execute("INSERT OR REPLACE INTO " + TABLE_NAME + "("+EMAIL+","+STUDENT_NAME+","+FATHER_NAME+","+MOTHER_NAME+","+AADHAR_NO+","+GENDER+","+CLASS12+","+CLASS10+","+STUDENT_ADDRESS+","+STUDENT_PHONE+")"+
            " VALUES(\""+str(email)+"\",\""+name+"\",\""+fathername+"\",\""+mothername+"\",\""+aadharno+"\",\""+gender+"\",\""+class12+"\",\""+class10+"\",\""+address+"\",\""+phone+"\")")

    con.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")



def destroyRootWindow():
    root.destroy()
    global secondWindow
    secondWindow = tk.Tk()
    secondWindow.title("Display results")
    secondWindow.geometry("1350x700")

    appLabel = tk.Label(secondWindow, text="JEE MAINS Registration",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

    tree.heading("zero", text="Student Name")
    tree.column("zero",anchor="center", width=100)
    tree.heading("one", text="Father Name")
    tree.column("one",anchor="center", width=100)
    tree.heading("two",text="Mother Name")
    tree.column("two",anchor="center", width=100)
    tree.heading("three", text="Aadhar Number")
    tree.column("three",anchor="center", width=80)
    tree.heading("four", text="Email")
    tree.column("four",anchor="center", width=120)
    tree.heading("five", text="Gender")
    tree.column("five", anchor="center", width=60)
    tree.heading("six", text="Class 12 Percent")
    tree.column("six", anchor="center", width=80)
    tree.heading("seven", text="Class 10 Percent")
    tree.column("seven", anchor="center", width=80)
    tree.heading("eight", text="Address")
    tree.column("eight",anchor="center", width=170)
    tree.heading("nine", text="Phone Number")
    tree.column("nine",anchor="center", width=110)
    c = sqlite3.connect("login.db")
    cursor = c.execute("SELECT * FROM " + TABLE_NAME + " WHERE email = ? ;",[username1])
    result = cursor.fetchall()
    i = 0
    for row in result:
        tree.insert('', i, text="Student %s"%(i+1),
                    values=(row[0], row[1],
                            row[2], row[3],
                            row[4], row[5],
                            row[6], row[7],
                            row[8], row[9],
                            ))
        i = i + 1

    tree.pack()
    Backbutton = tk.Button(secondWindow, text="Back to Login Page", command=lambda: backbutton(), cursor = "hand2")
    Backbutton.pack()

    secondWindow.mainloop()

def backbutton():
    secondWindow.destroy()
    login_page()


mainwindow()