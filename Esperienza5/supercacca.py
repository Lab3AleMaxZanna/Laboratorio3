import numpy as np 


 
import matplotlib.pyplot as plt 


 
from scipy.optimize import curve_fit 


 



 
f,Vin,Vout=np.loadtxt("Datifrequenza.txt", unpack=True) 


 
 


 
 


 
A= Vout/Vin 


 
df = np.zeros(len(f)) 


 
dA = A*0.03 


 
dlogA = dA/(A*2.3) 


 
plt.errorbar(f,np.log10(A),dlogA,df,'.') 


 
plt.title("Diagramma di Bode circuito invertente") 


 
plt.xscale("log") 


 
plt.show()  


 
plt.xlabel("log f") 


 
plt.ylabel("A(dB)") 


 
plt.show() 


 
 


 
s = f[f<23] 


 
amp = np.log10(A)[f<23] 


 
damp = dlogA[f<23] 


 
print(amp) 


 
 


 
print(s) 


 
 


 
 


 
init = (1,2) 


 
 


 
 


 
# errori 


 
sigma= damp 


 
w = 1/sigma**2  # errori dx non trascurabili, gli aggiungi a w, per conoscere f' del modello  


 
# fare un best fit fregandotene di delta xi 


 
 


 
 


 
 


 
 


 
# definire la funzione  


 
def h(x, a,b ): 


 
    return a*x + b 


 
     


 
 


 
pars,covm=curve_fit(h,s,amp,init,sigma,absolute_sigma=False) 


 
 


 
 


 
#calcolare chi2 


 
chi2 =( w*(amp-h(s,pars[0],pars[1]))**2).sum() 


 
 


 
#determinare ndof 


 
 


 
#ndof = len(x) -  len(init) 


 
print(pars) 


 
def g(x, a,b ): 


 
    return a*np.log10(x) + b 


 
xx = np.linspace(0.5,1000,1000) 


 
 


 
 


 
#plot della curva fit 


 
plt.plot(xx,g(xx,pars[0],pars[1]),color = 'green') 


 
 


 
 


 
s = f[f > 280] 


 
amp = np.log10(A)[f>280] 


 
damp = dlogA[ f>280] 


 
 


 
 


 
 


 
 


 
init = (1,2) 


 
 


 
 


 
# errori 


 
sigma= damp 


 
w = 1/sigma**2  # errori dx non trascurabili, gli aggiungi a w, per conoscere f' del modello  


 
# fare un best fit fregandotene di delta xi 


 
 


 
 


 
 


 
 


 
# definire la funzione  


 
 


 
     


 
 


 
pars1,covm=curve_fit(g,s,amp,init,sigma,absolute_sigma=False) 


 
 


 
print(pars1) 


 
#calcolare chi2 


 
chi2 =( w*(amp-g(s,pars1[0],pars1[1]))**2).sum() 


 
 


 
 


 
 


 
zz = np.linspace(100,2000,1000) 


 
 


 
 


 
#plot della curva fit 


 
plt.plot(zz,g(zz,pars1[0],pars1[1]),color = 'red') 


 
 


 
 