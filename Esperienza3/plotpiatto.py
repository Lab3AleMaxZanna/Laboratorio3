import numpy as np

import pylab 
import matplotlib
from scipy.optimize import curve_fit
x,y = pylab.loadtxt('GuadagnoInAmpiezza.txt', unpack = True)
dz= 0.04* np.ones(6)
pylab.errorbar(x,y/x,dz ,linestyle = '', color = 'black' , marker = 'o')
pylab.xlabel('$v_{in} (V)$')
pylab.ylabel('$v_{out}/v_{in}$')
pylab.rc('font',size = 18)
pylab.title('$A_v$')
pylab.minorticks_on()



# inizializzare i valori



# errori
 # errori dx non trascurabili, gli aggiungi a w, per conoscere f' del modello 
# fare un best fit fregandotene di delta xi


# definire la funzione 



#calcolare chi2


#determinare ndof

#ndof = len(x) -  len(init)


#print(chi2,ndof)

xx = np.linspace(min(x),max(x),1000)

t = 9.76*np.ones(len(xx))
#plot della curva fit
pylab.plot(xx,t,color = 'blue')



pylab.show()



