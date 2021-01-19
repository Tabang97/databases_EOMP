from tkinter import *
import mysql.connector
root = Tk()
root.geometry("700x600")
root.title("login page")
root.configure(background="skyblue")


# photo
photo = PhotoImage(file="images//download.png")
w = Label(root, image=photo)
w.place(x=80, y=0)

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoiceonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


# radiobutton func
r = IntVar()



# FULLNAME
lbluser = Label(root, text="Full Name", font="bold")
lbluser.place(x=110, y=180)
username = Entry(root, width=45)
username.place(x=110, y=210, width=300, height="30")

# ID
lblID = Label(root, text="ID No.", font="bold")
lblID.place(x=110, y=250)
password = Entry(root, width=45)
password.place(x=110, y=280, width=300, height="30")

# CONTACT
lblphone = Label(root, text="Contact No.", font="bold")
lblphone.place(x=110, y=320)
username = Entry(root, width=45)
username.place(x=110, y=350, width=300, height="30")

# ADDRESS
lbladdress = Label(root, text="Address", font="bold")
lbladdress.place(x=110, y=390)
username = Entry(root, width=45)
username.place(x=110, y=420, width=300, height="30")

# GENDER
gender = Label(root, text="Gender", font="bold")
gender.place(x=110, y=460)
radiobtn = Radiobutton(root, text="Male", variable=r, value=1)
radiobtn.place(x=230, y=460)
radiobtn2 = Radiobutton(root, text="Female", variable=r, value=2)
radiobtn2.place(x=330, y=460)

# BUTTON
btn = Button(root, text="Register", background="lime")
btn.place(x=200, y=550)



root.mainloop()
