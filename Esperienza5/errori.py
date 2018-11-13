import numpy as np 


 
import matplotlib.pyplot as plt 


 
from scipy.optimize import curve_fit 


 



 
f,Vin,Vout=np.loadtxt("Datifrequenza.txt", unpack=True) 





A= Vout/Vin 


 
df = f * 0.02 
print(df)


 
dA = A*0.03 


 
dlogA = dA/(A*2.3) 