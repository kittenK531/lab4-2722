import numpy as np
import matplotlib.pyplot as plt

#data=np.loadtxt('546.txt')
#plt.plot(data[0:76,0], data[0:76,1], lw=1.5, color="blue", label="trial 1")
#plt.plot(data[77:152,0], data[77:152,1], lw=1.5, color="red", label="trial 2")
#plt.plot(data[153:228,0], data[153:228,1], lw=1.5, color="orange", label="trial 3")
#plt.plot(data[229:304,0], data[229:304,1], lw=1.5, color="green", label="trial 4")
#plt.plot(data[305:380,0], data[305:380,1], lw=1.5, color="pink", label="trial 5")
#plt.plot(data[381:456,0], data[381:456,1], lw=1.5, color="purple", label="trial 6")
#plt.plot(data[457:532,0], data[457:532,1], lw=1.5, color="yellow", label="trial 7")

background = np.loadtxt('background_noLV.txt')
#plt.plot(background[0:76,0], background[0:76,1], lw=1.5, color="black", label="background")
bg = np.zeros((77,2),float)
bgcol2 = background[0:76,1]

for i in range(76):
    bg[i,1] = bgcol2[i]

i=0
Lambda = 544.4
wavelength = [f"{Lambda}_1",f"{Lambda}_2", f"{Lambda}_3", f"{Lambda}_4", f"{Lambda}_5", f"{Lambda}_6", f"{Lambda}_7"]
filename=f"{wavelength[i]}.txt"
color_arr = ["blue","red","green","orange","pink","purple","yellow"]
data=np.loadtxt(filename)

datacol1 = data[:,0]#; print(len(data[:,0]))
datacol2 = data[:,1]#; print(len(data[:,1]))

corr_col2 = datacol2 - bgcol2

for i in range(7):
    #plt.plot(datacol1, corr_col2, lw=1.5, color=color_arr[i], label="trial {0}".format(i+1))
    plt.plot(datacol1, datacol2, lw=1.5, color=color_arr[i], label="trial {0}".format(i+1))

plt.title(f"$\lambda = {Lambda}\;nm$")
plt.xlabel("$V_{CE}$")
plt.ylabel("$V_1$")
plt.legend()
plt.savefig(f'lab4_{Lambda}_noLV.png')
plt.show()
