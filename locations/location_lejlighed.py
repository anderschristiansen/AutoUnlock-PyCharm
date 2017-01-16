import matplotlib.pyplot as plt
import db

lat = db.lejlighed_location_lat
long = db.lejlighed_location_long

markers_on = [0]
plt.plot(long, lat, '-o', markersize=3)
plt.plot(long[0], lat[0], '-o', markersize=10) #grøn
plt.plot(long[-1], lat[-1], '-o', markersize=10) #rød

plt.show()