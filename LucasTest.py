import numpy as np
import time

def deltaT (k,del1):
    if k < 4 :
        delta = k*del1
    if k > 3 & k < 8 :
        delta = k*del1 + (k-3)
    if k == 8 :
        delta = k*del1 + 6
    if k == 9 :
        delta = k*del1 + 10
    
    return delta                # 7*6 + 4 = 46


def psquare(N):
    i = len(str(N)) -1
    nsf = int(str(N)[::-1])     # 273
    nx = (nsf % 10)**2
    nd = 0
    while i > 0:
        l = nsf % 10    # 3 7  
        lsn = 10*nx # 90 13690
        deltaInit = 2*(nd + l)         # 6 74
        
        nsf = int(nsf/10)       # 27
        
        time_startA = time.clock()
        k = nsf%10              # 7
        delta = deltaT(k,deltaInit)     # 46
        nx = (lsn+delta)*10 + (k**2%10) # 1369
        nd = 10*l   # 30
        i = i - 1
    

        

Num = int(2**1024 - 17)

psquare(Num)
