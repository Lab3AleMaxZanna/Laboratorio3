import numpy as np 


 
import matplotlib.pyplot as plt 


 
from scipy.optimize import curve_fit 
f,Vin,Vout=np.loadtxt("Datifrequenza.txt", unpack=True)
 
A= Vout/Vin  
df = np.zeros(len(f)) 
dA = A*0.03 
AdB = 20*np.log10(A)
DAdB= 20*dA/(A*2.3) 
print(DAdB)
plt.errorbar(f,AdB,DAdB,df,'.') 
plt.title("Diagramma di Bode circuito invertente") 


 
plt.xscale("log") 
plt.show()  


 
plt.xlabel("log f (kHz)")  
plt.ylabel("A(dB)") 
plt.show() 

s = f[f<23]  
amp = AdB[f<23] 


 
damp = DAdB[f<23] 


 


init = (1,2) 

# errori 
 
sigma= damp 


 
w = 1/sigma**2  # errori dx non trascurabili, gli aggiungi a w, per conoscere f' del 

def h(x, a,b ): 


 
    return a*np.log10(x) + b 

pars,covm=curve_fit(h,s,amp,init,sigma,absolute_sigma=False) 

#calcolare chi2 


 
chi2 =( w*(amp-h(s,pars[0],pars[1]))**2).sum() 

#determinare ndof 

#ndof = len(x) -  len(init) 

print(pars) 


 


xx = np.linspace(0.5,1000,1000) 


#plot della curva fit 


 
plt.plot(xx,h(xx,pars[0],pars[1]),color = 'green') 

s = f[f > 280] 


 
amp = AdB[f>280] 


 
damp = DAdB[ f>280] 


init = (1,2) 


 
# errori 


 
sigma= damp 


 
w = 1/sigma**2  # errori dx non trascurabili, gli aggiungi a w, per conoscere f' del modello  

 
p,covm=curve_fit(h,s,amp,init,sigma,absolute_sigma=False) 
print(p) 

 
chi2 =( w*(amp-h(s,p[0],p[1]))**2).sum()  
zz = np.linspace(100,2000,1000)  
plt.plot(zz,h(zz,p[0],p[1]),color = 'red') 


 
 


 
 