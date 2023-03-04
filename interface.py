from bode import *
from fourier import *
from math import sin, pi, sqrt, log
import matplotlib.pyplot as pyp
import numpy as np

def trait_sig():
    print(pi)
    print("Quel signal utiliser ?")
    print("1) Signal carré")
    print("2) Signal triangle")
    print("3) Signal perso.")
    inp = input(":")
    if inp == "1":
        sig_fun = carre
    elif inp == "2":
        sig_fun = triangle
    elif inp == "3":
        freq  = float(input("freq (Hz):"))
        omega = 2*pi*freq
        print("ex:4*4/pi")
        ampl  = eval(input("ampli:"))
        n = int(input("nb harmo:"))
        print("ex:1/(2*m+1)")
        ampl_harmo = input("mult sin (m):")
        const = float(input("const:"))
        print("ex:(2*m+1)")
        mult_sin = input("mult dans sin (m):")
        debut = int(input("debut:"))
        def sig_fun(x, a, o, harm):
            return ampl*sum([eval(ampl_harmo)*sin(eval(mult_sin)*omega*x) for m in range(debut, n+1)])
    print("Que faire avec le signal ?")
    print("1) Le plotter")
    print("2) Calculer les harmoniques")
    inp = input(":")
    if inp == "1":
        pts = int(input("nombre de points:"))
        periodes = int(input("périodes:"))
        plot_sig(freq, ampl, n, pts, periodes, sig_fun)
    elif inp == "2":
        print("TODO")



inp = ""
while inp != "q":
    print("Que souhaitez-vous faire ?")
    print("1) Traitement signal")
    print("2) Diagramme de Bode")
    inp = input(":")
    if inp == "1":
        trait_sig()
