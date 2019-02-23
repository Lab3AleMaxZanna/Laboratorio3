import numpy as np 


 
import matplotlib.pyplot as plt 


 
from scipy.optimize import curve_fit 
t,dt,v,dv=np.loadtxt("C:\\Users\\alexf\OneDrive\Desktop\laboratorio\Laboratorio3\Esperienza6\\nonnaLuisa.txt",unpack=True)
dt_eff=np.sqrt(dt**2+(dv/v*0.38)**2)

def func(x,a,b):
    return b*np.log(x/a)
popt,pcov=curve_fit(func,v,t,sigma=dt_eff)
print(popt,pcov)
plt.errorbar(v,t,dt,dv,'.')
x=np.linspace(1,10)
plt.plot(x,func(x,popt[0],popt[1]))
plt.xlabel("$V_{in}[V]$")
plt.ylabel("$\Delta t[ms]$")
plt.title("durata del segnale alto")
plt.show()