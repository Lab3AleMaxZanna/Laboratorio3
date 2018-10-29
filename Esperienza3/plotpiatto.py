import numpy

import pylab 
import matplotlib
from scipy.optimize import curve_fit
y,x,dy = pylab.loadtxt('misure.txt', unpack = True)

pylab.errorbar(x,y,dy ,linestyle = '', color = 'black' , marker = 'o')
pylab.xlabel('T[K]')
pylab.ylabel('p[Kpa]')
pylab.rc('font',size = 18)
pylab.title('best-fit')
pylab.minorticks_on()



# inizializzare i valori
init = (1)


# errori
sigma = dy
w = 1/sigma**2  # errori dx non trascurabili, gli aggiungi a w, per conoscere f' del modello 
# fare un best fit fregandotene di delta xi


# definire la funzione 
def f(x, a ):
    return 216.9*2.72**(a*(1/299.8-1/x))
    

pars,covm=curve_fit(f,x,y,init,sigma,absolute_sigma=False)


#calcolare chi2
chi2 =( w*(y-f(x,pars[0]))**2).sum()

#determinare ndof

#ndof = len(x) -  len(init)
print(pars)

#print(chi2,ndof)

xx = numpy.linspace(min(x),max(x),1000)


#plot della curva fit
pylab.plot(xx,f(xx,pars[0]),color = 'blue')



pylab.show()



