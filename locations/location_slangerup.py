import matplotlib.pyplot as plt
import db

lat = db.slangerup_location_lat
long = db.slangerup_location_long

plt.plot(long, lat, '-o', markersize=3)

plt.show()