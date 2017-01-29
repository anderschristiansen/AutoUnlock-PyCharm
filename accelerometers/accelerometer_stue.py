import matplotlib.pyplot as plt
import db
import pylab

fig = pylab.gcf()
fig.canvas.set_window_title('ACCELEROMETER STUE')

x = db.stue_acceleration_x
y = db.stue_acceleration_y
z = db.stue_acceleration_z
time = db.stue_timestamp

merged_acceleration = []
smooth_acceleration = []
smooth_time = []

for i, v in enumerate(x):
    avg = sum(v + y[i] + z[i]) / 3
    merged_acceleration.append(avg)

index = 0
for v in merged_acceleration[::10]:
    point = sum(merged_acceleration[index:index+10])/10
    #print(merged_acceleration[index:index+5])
    #print(point)
    smooth_acceleration.append(point)
    smooth_time.append(time[index])
    index += 10


########################################################################################################################
plt.figure(1)
########################################################################################################################
plt.subplot(221)
plt.plot(time, x, label='x')
plt.plot(time, y, label='y')
plt.plot(time, z, label='z')

plt.title('Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(222)
plt.plot(time, merged_acceleration, label='merged')

plt.title('Merged Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(223)
plt.plot(smooth_time, smooth_acceleration, label='smooth')

plt.title('Smooth Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.show()