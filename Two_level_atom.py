import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import complex_ode

def odes(x, t):

    # Cg and Ce are variables
    # delta and omega are constants

    hbar = 1.054*10**-34
    delta = 0
    omega = 1
    # Vectorises the coupled odes
    Cg = x[0]
    Ce = x[1]
    
    # DEfines each of the coupled odes
    Cgdt = 1/(hbar * 1j) * (-delta*Cg + (omega/2)*Ce)
    Cedt = 1/(hbar * 1j) * ((omega/2)*Cg + delta*Ce)

    return [Cgdt, Cedt]
    

def solve_ode(x0=[]):
    
    t = np.linspace(0,10**-32,1000)

    r = complex_ode(odes)

    x = odeint(r, x0, t)

    A = x[:,0]
    B = x[:,0]

    plt.plot(t,A)
    plt.plot(t,B)
    plt.show()




solve_ode([1, 0])

