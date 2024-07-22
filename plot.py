import matplotlib.pyplot as plt

RD_INIT = 0
PD_INIT = 9

START_POINT =260
END_POINT = 550

rd_data = []
pd_data = []
time = []

with open('tmsdata3.txt', 'r') as file:
    for line in file:
        data = line.strip().split(",")
        rd_data.append((float(data[3])-RD_INIT)*4.3)
        pd_data.append(float(data[5])-PD_INIT)
        time.append(float(data[1]))

START_TIME = time[START_POINT]
time = [ i - START_TIME for i in time]

plt.plot(time[START_POINT:END_POINT], rd_data[START_POINT:END_POINT])
plt.plot(time[START_POINT:END_POINT], pd_data[START_POINT:END_POINT])

plt.title('TMS results')
plt.xlabel('time')
plt.ylabel('data')

plt.show()
