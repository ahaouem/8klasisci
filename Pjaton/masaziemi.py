import math
import numpy as np

def massOfEarthUsingPendulum(lenghtOfPendulum, fallTime, earthDiameter, gravitationalConstant):
    #g = (((6.67 * 10**-11) * (5.972 * 10**24)) / (6371 * 1000)**2)
    g = (4*math.pi**2 * lenghtOfPendulum) / (fallTime**2)
    massOfEarth = g * ((earthDiameter)**2 / gravitationalConstant)
    return massOfEarth

def fallOfPendulum(lenghtOfPendulum, gravity):
    fallTime = math.sqrt(lenghtOfPendulum/gravity) * math.pi * 2
    return fallTime

earthDiameter = 6378.1 * 1000
gravitationalConstant = 6.67408 * (10 ** -11)
lenghtOfPendulum = 0.5
fallTime = 1.4179000000000004
listaPomiarow = [1.4, 1.39, 1.42, 1.4, 1.44, 1.4, 1.44, 1.41, 1.44, 1.39, 1.4, 1.42, 1.41, 1.44, 1.42, 1.42, 1.44, 1.41, 1.41, 1.44, 1.4, 1.41, 1.43, 1.41, 1.44, 1.43, 1.44, 1.43, 1.42, 1.42, 1.41, 1.43, 1.4, 1.44, 1.43, 1.41, 1.4, 1.39, 1.4, 1.4, 1.42, 1.43, 1.43, 1.4, 1.4, 1.43, 1.41, 1.43, 1.4, 1.42, 1.43, 1.4, 1.4, 1.43, 1.43, 1.39, 1.44, 1.41, 1.43, 1.41, 1.41, 1.42, 1.41, 1.43, 1.42, 1.43, 1.44, 1.4, 1.4, 1.44, 1.43, 1.4, 1.39, 1.41, 1.42, 1.44, 1.41, 1.43, 1.43, 1.44, 1.41, 1.44, 1.41, 1.43, 1.43, 1.44, 1.43, 1.44, 1.42, 1.43, 1.4, 1.4, 1.39, 1.4, 1.44, 1.41, 1.42, 1.43, 1.41, 1.39]

x = sum(listaPomiarow)/len(listaPomiarow)
odchylenie = np.std(listaPomiarow)

print("Wszystkie pomary:", listaPomiarow)
print("Błąd pomiarowy:", odchylenie)
print("Średnia:", x)
print("Masa ziemi:", massOfEarthUsingPendulum(lenghtOfPendulum, fallTime, earthDiameter, gravitationalConstant))
