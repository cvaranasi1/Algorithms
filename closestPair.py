# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:12:15 2020

@author: chand
"""

import numpy as np
#assert np  # silence pyflakes
numPts = int(1e5)
from numpy.random import Generator, PCG64
rg = Generator(PCG64(123456789))
#from numpy.random import default_rng
#rng = default_rng()
v = np.arange(-2e5,2e5,1,dtype='int64')
P = rg.choice(v,2*numPts,replace=False).reshape((2,numPts))

def closestPair(Px,Py): # Remember Px and Py are two copies of the same point-set; one sorted by x-coordinate and the other by y-coordinate
    if len(Px[0]) <=3:  # recursion will stop here at either 2 or 3 points
        d = 1e20
        for p in range (len(Px[0])-1):
            for q in range(p+1,len(Px[0])):
                dval = (Px[:,p][0] - Px[:,q][0])**2 + (Px[:,p][1] - Px[:,q][1])**2
                if dval <= d:
                    r = Px[:,p]
                    s = Px[:,q]
                    d = dval
        return d,r,s
    else:
        midX    =   Px[0][len(Px[0])//2] # Get the midpoint of X-coordinates
        Qx      =   Px[:,Px[0]<midX]     # All the points that are to the left of midX in Px
        Rx      =   Px[:,Px[0]>=midX]    # All the points to the right of midX in Px
        Qy      =   Py[:,Py[0]<midX]     # All the points--sorted by y-coordinates--that are to the left of midX in Py
        Ry      =   Py[:,Py[0]>=midX]    # All the points--sorted by y-coordinates--that are to the right of midX in Py
        dL,p1,q1   =   closestPair(Qx,Qy)   # Conquer the left-half
        dR,p2,q2   =   closestPair(Rx,Ry)   # Conquer the right-half
        if dL <= dR:
            delta = dL
            u1,v1 = p1,q1
        else:
            delta = dR
            u1,v1 = p2,q2
        # Now, compute splitPair
        Sy      =   Py[:,abs(Py[0]-midX)<=delta] # This is the set of points that are within 'delta' distance either way from midX and they are sorted by their y-coordinate
#        print(len(Sy))
        dc = 1e20
        for a in range (len(Sy[0])-1):
            for b in range(a+1,min(a+7,len(Sy[0]))):
                dval = (Sy[:,a][0] - Sy[:,b][0])**2 + (Sy[:,a][1] - Sy[:,b][1])**2
                if dval <= dc:
                    r1 = Sy[:,a]
                    s1 = Sy[:,b]
                    dc = dval
        if dc < delta:
            return dc, r1,s1
        else:
            return delta, u1, v1

Px = P[:,np.argsort(P[0])]    # Points sorted by x-axis coordinates
Py = P[:,np.argsort(P[1])]    # Points sorted by y-axis coordinates We will need later.
import time
st=time.time()
D, E, F = closestPair(Px,Py)
print("--- %s seconds for closestPair ---" % (time.time() - st))
print("\nClosest Pair:\t", E, F)
print("\nClosest distance:\t", np.sqrt(D))


    
    