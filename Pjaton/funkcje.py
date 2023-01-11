def main():
    #Code here
    pass

def parametr(x):
    print(x)

def r(x):
    return x

liczba_z_returna = r(x)

#Wywołanie funkcji

r(5) #Podajemy wartość x

parametr(10)

main()

#Zadania

#Zad 1
#Napisz funkcję square(x), która obliczy kwadrat podanej liczby x. Funkcja powinna zwrócić wynik.

#Zad 2 
#Napisz funkcję is_even(x), która sprawdzi, czy liczba x jest parzysta. Funkcja powinna zwrócić wartość True, jeśli liczba jest parzysta, lub False, jeśli jest nieparzysta.

#Zad 3
#Napisz funkcję min_of_three(x, y, z), która zwróci najmniejszą z trzech podanych liczb x, y, z

def square(x):
    return x**2

print(square(4))

def is_even(x):
    if x % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")

is_even(2)

def main_of_three(x, y, z):
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)

main_of_three(1, 2, 3)