import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd 
t=np.linspace(0,3,12*1024)
frec=np.array([164.81,130.81,246.93,220,164.81,174.61,196,174.61,164.81])
x=0
ti=0
tf=0.33
for i in range(9):
    x=x+np.reshape(np.sin(2*frec[i]*np.pi*t)*[t<=tf]*[t>=ti],np.shape(t))
    ti+=0.33
    tf+=0.33
plt.plot(t,x)
sd.play(x,3*1024)