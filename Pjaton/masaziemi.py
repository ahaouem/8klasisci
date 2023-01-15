import math

def massOfEarthUsingPendulum(lenghtOfPendulum, fallTime, earthDiameter, gravitationalConstant):
    g = (math.pi**2 * 2/fallTime ** 2) / lenghtOfPendulum * 2
    massOfEarth = g * (math.pow(earthDiameter, 2) /gravitationalConstant)
    return massOfEarth

def fallOfPendulum(lenghtOfPendulum, gravity):
    fallTime = math.sqrt(lenghtOfPendulum/gravity) * math.pi * 2
    return fallTime

earthDiameter = 6378.1 * 1000
gravitationalConstant = 6.67408 * (10 ** -11)
lenghtOfPendulum = 1
g = 9.81

fallOfPendulum(lenghtOfPendulum, g)
print(str(massOfEarthUsingPendulum(lenghtOfPendulum, fallOfPendulum(lenghtOfPendulum, g), earthDiameter, gravitationalConstant)) + "kg")
