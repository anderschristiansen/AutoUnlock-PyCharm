import sqlite3

db = sqlite3.connect('C:\@master\db\stue_AutoUnlock-1.db')
cursor = db.cursor()

sql_location = "SELECT * FROM location"
location = cursor.execute(sql_location)

#sql_accelerometer = "SELECT * FROM accelerometer"
#accelerometer = cursor.execute(sql_accelerometer)

data = location.fetchall ()

print(data)