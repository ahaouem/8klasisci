import math

# stałe
G = 6.67428e-11  # stała grawitacji
M = 5.9722e24  # masa Ziemi
R = 6371e3  # promień Ziemi

# okres wahadła
T = 2.83 * math.pi * math.sqrt(R / (G * M))

# masa Ziemi
mass = M

print(mass)
