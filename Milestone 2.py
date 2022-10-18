import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd 
from scipy.fftpack import fft
from scipy.signal import find_peaks

t=np.linspace(0,3,12*1024)
frec=np.array([164.81,130.81,246.93,220,164.81,174.61,196,174.61,164.81])
x=0
ti=0
tf=0.33
for i in range(9):
    x=x+np.reshape(np.sin(2*frec[i]*np.pi*t)*[t<=tf]*[t>=ti],np.shape(t))
    ti+=0.33
    tf+=0.33
#plt.plot(t,x)



fn1=np.random.randint(0,512,1)
fn2=np.random.randint(0,512,1)
noise=(np.sin(2*fn1*np.pi*t))+(np.sin(2*fn2*np.pi*t))


xt=x+noise

N=3*1024
f=np.linspace(0,512,int(N/2))
x_f=fft(xt)
x_f=2/N * np.abs(x_f[0:np.int(N/2)])

x_f1=fft(x)
x_f1=2/N * np.abs(x_f1[0:np.int(N/2)])

i=0
maxx=x_f1[0]

while i<len(x_f1):
    if (x_f1[i]>maxx):
      maxx=x_f1[i]
    i+=1
 
peaks , _ = find_peaks(x_f,height=[maxx+1,5])
print(peaks)




o=np.round(f[peaks[0]])
h=np.round(f[peaks[1]])
 
xf=xt-(np.sin(2*np.pi*o*t)+np.sin(2*np.pi*h*t))

xft=fft(x)
xft=2/N * np.abs(x_f1[0:np.int(N/2)])


plt.subplot(3,1,1)
plt.plot(t,x)
plt.subplot(3,1,2)
plt.plot(t,xt)
plt.subplot(3,1,3)
plt.plot(t,xf)

plt.figure()
plt.subplot(3,1,1)
plt.plot(x_f1)
plt.subplot(3,1,2)
plt.plot(x_f)
plt.subplot(3,1,3)
plt.plot(xft)
sd.play(x,3*1024)
