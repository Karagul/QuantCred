'''
QuantCred
=========

Copyright 2017 @ Michael Kovarik
(See LICENSE file)

In the following, Q is represents the survival curve (a function
accepting a float and returning a float), Z represents the discount
curve (similar to Q), and R is the recovery rate (a float from 0
to 1).
'''
from scipy.integrate import quad


# CREDIT DERIVATIVE PRICING

def RPV01_continuous(Q, Z, T):
    I = lambda t: Q(t) * Z(t)
    return quad(I, 0, T)[0]

def RPV01_discrete(Q, Z, T, tenors):
    pass
