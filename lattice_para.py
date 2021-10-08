#! /usr/bin/env python
import math
import numpy as np
a,E = np.loadtxt('data',usecols=(0,1),delimiter='\t',unpack = True)
# a is the list of sclaing factors in the test calculation
# E is the list of energies
x=(a*2.8664)**(-2)
p=np.polyfit(x,E,3)
c0=p[3]
c1=p[2]
c2=p[1]
c3=p[0]
x1=(math.sqrt(4*c2**2-12*c1*c3-2*c2))/(6*c3)
Lpara=math.sqrt(x1)**(-1)
print 'the final lattice parameter is : %s '%(Lpara)
