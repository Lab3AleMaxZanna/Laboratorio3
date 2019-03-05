import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Vin,Vout,f,phi,dphi=np.loadtxt("C:\\Users\\alexf\OneDrive\Desktop\laboratorio\Laboratorio3\Esperienza5\integratorefrequenza.txt", unpack=True)
f=f*1000
Vin=Vin[f<100000]
Vout=Vout[f<100000]
phi=phi[f<100000]
dphi=dphi[f<100000]
f=f[f<100000]
Vin=Vin[f>40]
Vout=Vout[f>40]
phi=phi[f>40]
dphi=dphi[f>40]
f=f[f>40]
plt.figure(1)
plt.errorbar(f,20*np.log10(Vout/Vin),20*(3*1.414/100)*np.ones(len(Vin)),None,'.')
plt.xscale("log")
plt.xlabel("frequenza[Hz]")
plt.ylabel("guadagno[dB]")

plt.figure(2)
plt.plot(f,phi,'.')
plt.xscale("log")
plt.xlabel("frequenza[Hz]")
plt.ylabel("Fase[gradi]")
plt.figure(3)
x=np.logspace(1,5,10000)
plt.xlabel("frequenza[Hz]")
plt.ylabel("Fase[gradi]")
def ang(f):
    return 180-180/np.pi*np.arctan(f*10**-2)
plt.plot(x,ang(x))  
plt.xscale("log")
plt.show()