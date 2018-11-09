import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
Vin,Vout,f,phi,dphi=np.loadtxt("C:\\Users\\alexf\OneDrive\Desktop\laboratorio\Laboratorio3\Esperienza5\integratorefrequenza.txt", unpack=True)
plt.plot(f,20*np.log10(Vout/Vin),'.')
plt.xscale("log")
plt.show()
