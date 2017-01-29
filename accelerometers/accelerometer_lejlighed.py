import matplotlib.pyplot as plt
import db
import pylab

fig = pylab.gcf()
fig.canvas.set_window_title('ACCELEROMETER LEJLIGHED')

x = db.lejlighed_acceleration_y
y = db.lejlighed_acceleration_y
z = db.lejlighed_acceleration_z
time = db.lejlighed_timestamp

merged_acceleration = []

for i, v in enumerate(x):
    avg = sum(v + y[i] + z[i]) / 3
    merged_acceleration.append(avg)

plt.figure(1)

plt.subplot(211)
plt.plot(time, x, label='x')
plt.plot(time, y, label='y')
plt.plot(time, z, label='z')

plt.title('Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')

plt.subplot(212)
plt.plot(time, merged_acceleration, label='merged')

plt.title('Merged Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')

plt.show()