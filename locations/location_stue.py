import matplotlib.pyplot as plt
import db

lat = db.stue_location_lat
long = db.stue_location_long

plt.plot(long, lat, '-o', markersize=3)

plt.show()

#print (location)
#print(longitude1[0], latitude1[0])

#plt.plot(longitude1, latitude1)
#plt.plot(longitude1[0:10], latitude1[0:10], 'ro')
#plt.axis([10, 20, 50, 60])