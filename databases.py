import mysql.connector
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoiceonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

sql = "UPDATE Dentists SET Dentists_Surname = 'myberg' WHERE Dentists_Name = Godwin"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute('SELECT * FROM Dentists')
for i in mycursor:
    print(i)
