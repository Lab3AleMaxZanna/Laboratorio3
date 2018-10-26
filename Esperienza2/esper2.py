import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def merge(array1:np.array, array2:np.array) -> np.array:
    """merge two unidimensional array of the same dtype"""
    assert array1.dtype == array2.dtype
    assert len(array1.shape) == 1
    assert len(array2.shape) == 1
    array3 = np.empty((len(array1) + len(array2),), dtype=array1.dtype)
    array3[:len(array1)]=array1
    array3[len(array1):]=array2
    return array3

#INSERISCI  Nomi da dare ad x e y (con unità di misura)
namex="$V_{in}$ [V]"
namey="$V_{out}$ [V]"
#INSERISCI variabile x,y
f1,df1,Vout1=np.loadtxt("data0.txt",unpack=True)
f2,Vout2,dVout2=np.loadtxt("data1.txt",unpack=True)

f=merge(f1, f2)
df = merge(df1, 3/100 * f2)
Vout = merge(Vout1, Vout2*2)
dVout = merge(3/100 * Vout1, dVout2*2) 
#GuaDAGNO IN FREQUENZA
Vin=np.ones(len(Vout))*2.48
Vin[0]=2.46

dB=20*np.log(Vout/Vin)
ddB = 20*dVout/Vout

def att(x, ft):
    return  np.log(1/np.sqrt(1+np.square(x/ft)))*20
    
popt,pcov=curve_fit(att,f,dB,p0=None,sigma=ddB)
ft=popt[0]
perr=np.sqrt(np.diagonal(pcov))
dft=perr[0]
    
t=np.linspace(min(f),max(f),1000)
plt.figure(0)
plt.errorbar(f,dB,ddB,df,'.')
#plt.plot(t,att(t, 5.1))
plt.plot(t,att(t, ft))
plt.xscale("log")
plt.grid(color='gray')
plt.xlabel("Frequenza (kHz)")
plt.ylabel("Guadagno (dB)")
#INSERISCI IL TITOLO
plt.title('Filtro passa-basso (ft = {} kHz)'.format(ft))

chi=sum((dB-att(f,ft))**2/ddB**2)
print("il chi quadro è "+str(chi))


plt.show()

'''
#INSERISCI limiti del grafico
    
print("i tuoi dati sono:\n",x,"\n",y)

#funzione di fit
def f(x,m,q):
    return m*x+q
#grafico dei soli punti
plt.figure(1)
plt.errorbar(x,y,dy,dx,linestyle=' ',marker='o')
plt.grid(color='gray')
plt.xlabel(namex)
plt.ylabel(namey)
#INSERISCI IL TITOLO
plt.title('Dati raccolti')
plt.xlim(limx[0],15)
plt.ylim(limy[0],limy[1])

plt.savefig("data.jpeg")
plt.show()
#fit linerare
popt,pcov=curve_fit(f,x,y,p0=None,sigma=dy)
m=popt[0]
q=popt[1]
perr=np.sqrt(np.diagonal(pcov))
dm=perr[0]
dq=perr[1]
print("la pendenza è "+str(m)+"+-"+str(dm)+ "\nl'intercetta vale "+str(q)+"+-"+str(dq))
#grafico con il fit
plt.figure(2)
t=np.linspace(0,11,200)
plt.plot(t,f(t,m,q))
plt.errorbar(x,y,dy,dx,linestyle=' ',marker='.')
plt.grid(color='gray')
plt.xlabel(namex)
plt.ylabel(namey)
#INSERISCI IL TITOLO
plt.title('Fit lineare dei dati')

plt.xlim(limx[0],limx[1])
plt.ylim(0,4)
plt.savefig("linfit.jpeg")
plt.show()
#ESEGUE test chi2
chi=0
for i in range (len(x)):
    chi=(y[i]-f(x[i],m,q))**2/dy[i]**2
print("il chi quadro è "+str(chi))
for i in range(len(x)):
    print(str(x[i])+" & "+str(dx[i])+" & "+str(y[i])+" & "+str(dy[i])+" & "+str(ra[i])+" & "+str(dra[i])+" \\"+"\\")

'''