import matplotlib.pyplot as plt
import db

x = db.slangerup_acceleration_x
y = db.slangerup_acceleration_y

markers_on = [0]
plt.plot(x, y, '-o', markersize=3)
plt.plot(x[0], y[0], '-o', markersize=10) #grøn
plt.plot(x[-1], y[-1], '-o', markersize=10) #rød

plt.show()