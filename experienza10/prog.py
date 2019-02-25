import numpy as np  
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 
Vi,dVi,Vout,dVout=np.loadtxt("C:\\Users\\alexf\OneDrive\Desktop\laboratorio\Laboratorio3\experienza10\dati.txt",unpack=True)
a=np.loadtxt("C:\\Users\\alexf\OneDrive\Desktop\laboratorio\Laboratorio3\experienza10\dati.txt",unpack=True)
print(a[0][5])
for i in range(len(a[0])):
        print(str(a[0][i])+"&"+str(a[1][i])+"&"+str(a[2][i])+"&"+str(a[3][i])+"\\\ \hline")






plt.errorbar(Vi,Vout,dVout,dVi,'.')
plt.ylabel("$V_{out}[V]$")
plt.xlabel("$V_{in}[V]$")
plt.title("Relazione tensione in ingresso/uscita per il componente NOT")
plt.show()
