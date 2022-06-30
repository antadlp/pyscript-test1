import numpy as np

def catenary(**kwargs):
    
    a= kwargs.get("a", 1)
    x = kwargs.get("x", np.linspace(0, 1, 100))
    c = kwargs.get("c", 0)
    
    return np.divide(np.cosh(a*x), a) + c
    