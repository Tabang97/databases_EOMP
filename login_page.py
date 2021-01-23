from tkinter import *
import mysql.connector
from tkinter import messagebox


root = Tk()
root.geometry("500x600")
root.title("login page")
root.configure(background="skyblue")

# photo
photo = PhotoImage(file="images//download.png")
w = Label(root, image=photo)
w.place(x=80, y=0)
# background = PhotoImage(file="images//2-nature-wallpaper-grass.png")
# w = Label(root, image=background)
# w.place(x=0, y=0)


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoiceonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


# register function
def register():
    root.destroy()
    import register





# Login function
def log():
    users = username.get()
    passs = password.get()
    sql = "select * from Login where username = %s and password = %s"
    mycursor.execute(sql, [users, passs])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()
#

def logged():
    messagebox.showinfo("Successfully", "You have successfully logged")
    root.destroy()
    import Admin_login


# if login details are incorrect
def failed():
    messagebox.showinfo("Error", "try again")
    Username.delete(0, END)
    Password.delete(0, END)


# USERNAME
lbluser = Label(root, text="username", font="bold")
lbluser.place(x=110, y=170)
username = Entry(root, width=45)
username.place(x=110, y=200, width=200, height="30")

# PASSWORD
lblpassword = Label(root, text="password", font="bold")
lblpassword.place(x=110, y=250)
password = Entry(root, width=45, show="*")
password.place(x=110, y=300, width=200, height="30")

# BUTTON
btn = Button(root, text="Login", background="lime", command=log)
btn.place(x=170, y=360)

jstlbl = Label(root, text="__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________", background="skyblue")
jstlbl.place(x=0, y=390)

# Register button
btn = Button(root, text="Register user", background="lime", command=register)
btn.place(x=140, y=440)

root.mainloop()
