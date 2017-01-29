import matplotlib.pyplot as plt
import db
import pylab

fig = pylab.gcf()
fig.canvas.set_window_title('ACCELEROMETER X-Y-Z MERGED')

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
plt.subplot(221)
plt.plot(s_time, s_x, label='x')
plt.plot(s_time, s_y, label='y')
plt.plot(s_time, s_z, label='z')
plt.title('Stue - Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(222)
plt.plot(s_time, s_merged_acceleration, label='merged')
plt.title('Stue - Merged Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(223)
plt.plot(l_time, l_x, label='x')
plt.plot(l_time, l_y, label='y')
plt.plot(l_time, l_z, label='z')
plt.title('Lejlighed - Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################
plt.subplot(224)
plt.plot(l_time, l_merged_acceleration, label='merged')
plt.title('Lejlighed - Merged Acceleration')
plt.legend(loc='upper right')
plt.xlabel('Milliseconds')
plt.ylabel('M/s^2')
########################################################################################################################





########################################################################################################################
#plt.subplot(223)
#plt.plot(s_smooth_time, s_smooth_acceleration, label='smooth')
#plt.title('Smooth Acceleration')
#plt.legend(loc='upper right')
#plt.xlabel('Milliseconds')
#plt.ylabel('M/s^2')
########################################################################################################################
plt.show()