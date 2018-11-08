import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
f,Vin,Vout=np.loadtxt("C:\\Users\\alexf\OneDrive\Desktop\laboratorio\Laboratorio3\Esperienza5\Datifrequenza.txt", unpack=True)
plt.plot(f,np.log10(Vout/Vin),'.')
plt.xscale("log")
plt.show()