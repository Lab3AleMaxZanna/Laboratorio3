import numpy as np 


 
import matplotlib.pyplot as plt 


 
from scipy.optimize import curve_fit 


 



 
Vin,Vout,f ,phi ,dphi=np.loadtxt("integratorefrequenza.txt", unpack=True) 


F= f[f< 82]

vin= Vin[f< 82]
vout = Vout[f< 82]
dF = np.zeros(len(F)) 
AdB = 20* np.log10(vout/vin)
fase = phi[f<82]
Dadb = 0.26*np.ones(len(AdB) )
dfase = 0.04* fase
plt.errorbar( F,AdB,Dadb, None ,'.')
plt.xlabel("log f(kHz)")
plt.ylabel("$\phi ( ^\circ)$")
plt.xscale("log")
plt.show()





