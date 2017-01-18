import matplotlib.pyplot as plt
import db

x = db.test_acceleration_x
y = db.test_acceleration_y
z = db.test_acceleration_z
time = db.test_timestamp

markers_on = [0]
plt.plot(time[0:1000], z[0:1000], '-o', markersize=3)
plt.plot(time[0], z[0], '-o', markersize=10) #grøn
#plt.plot(time[-1], z[-1], '-o', markersize=10) #rød

#plt.bar(1 + 0.00, x, color = 'b', width = 0.25)
#plt.bar(1 + 0.25, y, color = 'g', width = 0.25)
#plt.bar(1 + 0.50, z, color = 'r', width = 0.25)

plt.show()