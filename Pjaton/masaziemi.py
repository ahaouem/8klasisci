import math

# Wartości początkowe
L = 2  # długość ramienia wahadła
g = 9.81  # przyspieszenie ziemskie
T = [2.70, 2.85, 2.82, 2.90, 2.87, 2.83, 2.76, 2.91, 2.65, 2.89, 2.88, 2,90]  # okres wahadła

# Obliczanie masy za pomocą wzoru
m = (4 * math.pi**2 * L) / (g * T**2)

print("Masa Ziemi:", m, "kg")
