import sqlite3

db_stue = sqlite3.connect('C:\@master\db\stue.db')
db_slangerup = sqlite3.connect('C:\@master\db\slangerup.db').cursor()
db_lejlighed = sqlite3.connect('C:\@master\db\lejlighed.db').cursor()

db_kor_0 = sqlite3.connect('C:\@master\db\korrekte-lomme\AutoUnlock-0.db').cursor()

#db_ukor_1 = sqlite3.connect('C:\@master\db\korrekteU-lomme\kortAutoUnlock-1.db').cursor()



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
sql_acceleration_z = "SELECT acceleration_z FROM accelerometer"
sql_timestamp = "SELECT timestamp FROM accelerometer"

lejlighed_acceleration_x = db_lejlighed.execute(sql_acceleration_x).fetchall()
lejlighed_acceleration_y = db_lejlighed.execute(sql_acceleration_y).fetchall()
lejlighed_acceleration_z = db_lejlighed.execute(sql_acceleration_z).fetchall()
lejlighed_timestamp = db_lejlighed.execute(sql_timestamp).fetchall()

slangerup_acceleration_x = db_slangerup.execute(sql_acceleration_x).fetchall()
slangerup_acceleration_y = db_slangerup.execute(sql_acceleration_y).fetchall()

stue_acceleration_x = db_stue.execute(sql_acceleration_x).fetchall()
stue_acceleration_y = db_stue.execute(sql_acceleration_y).fetchall()
stue_acceleration_z = db_stue.execute(sql_acceleration_z).fetchall()
stue_timestamp = db_stue.execute(sql_timestamp).fetchall()

kor_acceleration_x = db_kor_0.execute(sql_acceleration_x).fetchall()
kor_acceleration_y = db_kor_0.execute(sql_acceleration_y).fetchall()
kor_acceleration_z = db_kor_0.execute(sql_acceleration_z).fetchall()
kor_timestamp = db_kor_0.execute(sql_timestamp).fetchall()

#ukor_acceleration_x = db_ukor.execute(sql_acceleration_x).fetchall()
#ukor_acceleration_y = db_ukor.execute(sql_acceleration_y).fetchall()
#ukor_acceleration_z = db_ukor.execute(sql_acceleration_z).fetchall()
#ukor_timestamp = db_ukor.execute(sql_timestamp).fetchall()
