#!/usr/bin/env python3
from math import pi
import matplotlib.pyplot as pyp


def carre(x, ampl, omega, n):
    return (ampl*4/pi)*sum([ 1/(2*m+1) * sin((2*m+1)*omega*x) for m in range(n+1)])

def triangle(x, ampl, omega, n):
    return (ampl*8/(pi**2))*sum([ ((-1)**m)/((2*m+1)**2) * sin((2*m+1)*omega*x) for m in range(n+1)])

def plot_sig(freq: float, ampl: float, n: int, pts: int, periodes: int, f):
    """
    freq: fréquence du signal
    ampl: amplitude du signal
    n: nombre d'harmoniques
    pts: nombres de points
    periodes: nombre de périodes à afficher
    f: fonction du signal prennant en argument (temps, amplitude, pulsation, nombre d'harmoniques)
    """
    omega = 2*pi*freq

    x = []
    y = []
    pas = periodes/(freq*pts)
    for i in range(pts+1):
        x.append(i*pas)
        y.append(f(i*pas, ampl, omega, n))

    pyp.plot(x, y)
    pyp.xlabel("temps")
    pyp.ylabel("tension")
    pyp.show()

if __name__ == "__main__":
    from math import log, sqrt, sin, pi
    import matplotlib.pyplot as pyp
    plot_sig(100, 2, 100, 1000, 2, carre)
