QuantCred
=========

Quantcred is a credit derivatives pricing toolkit written in Python 3.
Refer to *Modelling Single-Name and Multi-name Credit Derivatives* by
Dominic O'Kane for the underlying theory.


Survival curves
---------------

Pricing credit derivatives requires first having a model of default
probabilities. Such models produce survival curves $Q(t)$, which is the
probability that the creditor has not defaulted up to time $t>0$ years
into the future.

Survival curves $Q(t)$ need to satisfy the following three properties:

1. $Q(0) = 1$
2. $Q'(t)$ exists, and
3. $Q'(t) < 0$.

Associated with the survival curve is the *hazard rate* $\lambda (t)$,
defined by 

$$\lambda(t) = - \frac{Q'(t)}{Q(t)}.$$

In QuantCred, survival curves are given by functions of the form 
`float -> float`. For example:

``````````````````````````````````````````````````````````````````python
from math import exp

def surv_curve(t: float) -> float:
    return exp(-0.005 * t)
``````````````````````````````````````````````````````````````````

This function would define a survival curve with a constant hazard rate
of 0.5%/year.
