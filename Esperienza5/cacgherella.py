import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
Vin,Vout=np.loadtxt("C:\\Users\\alexf\OneDrive\Desktop\laboratorio\Laboratorio3\Esperienza5\Datiampiezza.txt", unpack=True)
Vout=Vout[Vin<2.94]
Vin=Vin[Vin<2.94]
A=Vout/Vin
plt.figure(1)
plt.subplot(2,1,1)
plt.errorbar(Vin,Vout,Vout*0.03,Vin*0.03,'.')

def cost (x,a):
    return a+o*x
popt,pcov=curve_fit(retta,Vin,A,sigma=A*0.03*1.414)
print(popt)
x=np.linspace(0,3)
plt.plot(x,popt[0]*x)

plt.subplot(2,1,2)
plt.errorbar(Vin,Vout-Vin*popt[0],Vout*0.03,Vin*0.03,'.')
plt.plot(x,0*x)

plt.figure(2)
plt.errorbar(Vin,A,A*0.03*1.414,None,'.')
plt.plot(x,np.ones(len(x))*np.mean(A))
plt.xlabel("$ V_{in}[V]$")
plt.ylabel("Guadagno $V_{out}/V_{in}$")
print(pcov,popt)
chi=0
for i in range(len(A)):
    chi+=(A[i]-np.mean(A))**2/(A[i]*0.03*1.414)**2
print(chi)

plt.show()
