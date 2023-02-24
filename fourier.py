#!/usr/bin/env python3
from math import log, sqrt, sin, pi
import matplotlib.pyplot as pyp

def sig_carre(freq: float, ampl: float, n: int, pts: int, periodes: int):

    omega = 2*pi*freq
    def f(x):
        return (ampl*4/pi)*sum([ 1/(2*m+1) * sin((2*m+1)*omega*x) for m in range(n+1)])

    x = []
    y = []
    pas = periodes/(freq*pts)
    for i in range(pts+1):
        x.append(i*pas)
        y.append(f(i*pas))

    pyp.plot(x, y)
    pyp.show()

sig_carre(100, 2, 100, 1000, 2)
