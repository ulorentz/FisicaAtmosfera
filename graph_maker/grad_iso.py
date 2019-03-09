#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

#to set latex font in matplotlib
params = {
    "text.usetex" : True,
    "font.size" : 13,
    "font.family" : "serif",
    "text.usetex": True, 
    "pgf.rcfonts": False,   
    "pgf.preamble": [
         "\\usepackage{units}",         
         "\\usepackage{metalogo}",
         "\\usepackage{unicode-math}",  
         r"\setmathfont{xits-math.otf}",
         r"\setmainfont{DejaVu Serif}", 
         ]         
}
plt.rcParams.update(params) 


# To print graph regarding comparison between isothermal atmosphere and mean 
# tropospherical gradient

t_0=300.
p_0=1000.
p_top=200.
t_mean=260.

def iso_ztop(p, p_0, t_mean):
    return -(t_mean*8.31/(0.029*9.81))*np.log(p/p_0)
def grad_ztop(p, p_0, t_0):
    return t_0*(1-np.power(p/p_0, 8.314*0.0065/(0.029*9.81)))/0.0065

press=np.linspace(p_0, p_top, 100)

plt.figure(0, figsize=(6.4*0.9,4.8*0.9))
plt.plot(press, iso_ztop(press, p_0, t_mean), label="Atmosfera isoterma")
plt.plot(press, grad_ztop(press, p_0, t_0), label="Gradiente medio")
plt.ylabel("m")
plt.xlabel("hPa")
plt.legend()
plt.grid()
plt.savefig("../figures/iso_vs_grad.pdf", format="pdf")
#plt.show()
