#!/usr/bin/env python3
from math import log,sqrt
import matplotlib.pyplot as pyp

def V2dBV(tension: float) -> float:
    return 20*log(u_eff(tension), 10)

def A2dB(amplification: float) -> float:
    return 20*log(amplification, 10)

def dBV2V(niveau: float) -> float:
    return pow(10, niveau/20)

def u_eff(tension: float) -> float:
    return tension/sqrt(2)

def plot_freq_ampli(frequences: list, amplifications: list):
    gains = [A2dB(i) for i in amplifications]
    pyp.plot(frequences, gains)
    pyp.xscale("log")
    pyp.xticks(frequences, frequences)
    pyp.show()

def plot_freq_phase(frequences: list, phases: list):
    pyp.plot(frequences, phases)
    pyp.xscale("log")
    pyp.xticks(frequences, frequences)
    pyp.show()

plot_freq_ampli([100, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 7000, 10000, 20000, 30000, 50000, 70000, 100000], \
                  [5, 5, 5, 5, 4.999, 4.996, 4.937, 4.705, 3.536, 2.273, 1.213, 0.312, 0.139, 0.05, 0.026, 0.012])
