# Mamy dwa typy pętli: for & while
# Pętla for
# for zmienna in zakres:
#     instrukcja
# Zakres może być wyrażeniem generującym

# Pętla while
# while warunek:
#     instrukcja

# Przykład pętli for
for i in range(10):
    print(i)

# Przykład pętli while
i = 0
while i < 10:
    print(i)
    i += 1
    
# Pętle while można zastopować używając polecenia "break"
# Oto przykład programu, który drukuje liczby od 1 do 10, ale kończy drukowanie po wyświetleniu liczby 5, używając instrukcji break:
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Pętle while można pominąć używając polecenia "continue"
# Oto przykład programu, który drukuje liczby od 1 do 10, ale pomija liczbę 5, używając instrukcji continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)




# Zadania
# Napisz program, który wyświetla liczby od 1 do 10.
# Napisz program, który wyświetla kwadraty liczb od 1 do 10.
# Napisz program, który sumuje liczby od 1 do 100.










