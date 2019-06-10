import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
fig= plt.figure(figsize=(5,4))

ax1 = fig.add_subplot(111)


def animate(i):
    pullData = open("machine1.txt","r").read()
    pullData2 = open("machine2.txt","r").read()
    pullData3 = open("machine3.txt","r").read()
    xar = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    yar1 = []
    yar2 = []
    yar3 = []
    for i in range(0,24):
        yar1.append(int(pullData.count(xar[i])))
        yar2.append(int(pullData2.count(xar[i])))
        yar3.append(int(pullData3.count(xar[i])))
    ax1.clear()
    ax1.plot(xar,yar1,label = 'Machine 1')
    ax1.plot(xar,yar2, label = 'Machine 2')
    ax1.plot(xar,yar3, label = 'Machine 3')
    ax1.legend(loc='upper center',fontsize = 'x-small')
    ax1.set_xlabel('Time', size = 6)
    ax1.set_ylabel('Machine Access', size = 5)
    for xc in xar:
        plt.axvline(x=xc, color='lightgray', linestyle=':')
ani = animation.FuncAnimation(fig, animate, interval=1000)


plt.show()
fig.savefig('UPR_TimeGraph_square.png',bbox_inches='tight')

