from tkinter import messagebox
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoiceonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
root = Tk()
root.geometry("500x400")
root.title("Admin page")
root.configure(background="white")

root.mainloop()
