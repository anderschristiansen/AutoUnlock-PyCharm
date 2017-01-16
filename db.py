import sqlite3

db_stue = sqlite3.connect('C:\@master\db\stue.db')
db_slangerup = sqlite3.connect('C:\@master\db\slangerup.db').cursor()
db_lejlighed = sqlite3.connect('C:\@master\db\lejlighed.db').cursor()


# LOCATION
sql_latitude = "SELECT latitude FROM location"
sql_longitude = "SELECT longitude FROM location"

stue_location_lat = db_stue.execute(sql_latitude).fetchall()
stue_location_long = db_stue.execute(sql_longitude).fetchall()

slangerup_location_lat = db_slangerup.execute(sql_latitude).fetchall()
slangerup_location_long = db_slangerup.execute(sql_longitude).fetchall()

lejlighed_location_lat = db_lejlighed.execute(sql_latitude).fetchall()
lejlighed_location_long = db_lejlighed.execute(sql_longitude).fetchall()

# ACCELEROMETER
sql_acceleration_x = "SELECT acceleration_x FROM accelerometer"
sql_acceleration_y = "SELECT acceleration_y FROM accelerometer"

lejlighed_acceleration_x = db_lejlighed.execute(sql_acceleration_x).fetchall()
lejlighed_acceleration_y = db_lejlighed.execute(sql_acceleration_y).fetchall()


