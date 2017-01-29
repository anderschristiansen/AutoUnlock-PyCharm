import matplotlib.pyplot as plt
import db
import pylab

fig = pylab.gcf()
fig.canvas.set_window_title('ACCELEROMETER X-Y-Z')

s_x = db.stue_acceleration_x
s_y = db.stue_acceleration_y
s_z = db.stue_acceleration_z
s_time = db.stue_timestamp

l_x = db.lejlighed_acceleration_x
l_y = db.lejlighed_acceleration_y
l_z = db.lejlighed_acceleration_z
l_time = db.lejlighed_timestamp

s_merged_acceleration = []
s_smooth_acceleration = []
s_smooth_time = []

l_merged_acceleration = []
l_smooth_acceleration = []
l_smooth_time = []

for i, v in enumerate(s_x):
    avg = sum(v + s_y[i] + s_z[i]) / 3
    s_merged_acceleration.append(avg)

for i, v in enumerate(l_x):
    avg = sum(v + l_y[i] + l_z[i]) / 3
    l_merged_acceleration.append(avg)

index = 0
for v in s_merged_acceleration[::10]:
    point = sum(s_merged_acceleration[index:index+10])/10
    #print(merged_acceleration[index:index+5])
    #print(point)
    s_smooth_acceleration.append(point)
    s_smooth_time.append(s_time[index])
    index += 10

index = 0
for v in l_merged_acceleration[::10]:
    point = sum(l_merged_acceleration[index:index+10])/10
    #print(merged_acceleration[index:index+5])
    #print(point)
    l_smooth_acceleration.append(point)
    l_smooth_time.append(l_time[index])
    index += 10


########################################################################################################################
plt.figure(1)
########################################################################################################################
plt.subplot(331)
plt.tight_layout(pad=0.8, w_pad=0.8, h_pad=2.0)
plt.plot(s_time, s_x, label='x')
plt.title('Stue - Acceleration X')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(332)
plt.plot(s_time, s_y, label='y')
plt.title('Stue - Acceleration Y')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(333)
plt.plot(s_time, s_z, label='z')
plt.title('Stue - Acceleration Z')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(334)
plt.plot(l_time, l_x, label='x')
plt.title('Lejlighed - Acceleration X')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(335)
plt.plot(l_time, l_y, label='y')
plt.title('Lejlighed - Acceleration Y')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(336)
plt.plot(l_time, l_z, label='z')
plt.title('Lejlighed - Acceleration Z')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')





########################################################################################################################
#plt.subplot(223)
#plt.plot(s_smooth_time, s_smooth_acceleration, label='smooth')
#plt.title('Smooth Acceleration')
#plt.legend(loc='upper right')
#plt.xlabel('Milliseconds')
#plt.ylabel('M/s^2')
########################################################################################################################
plt.show()