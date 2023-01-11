# Lista w Pythonie jest to sekwencyjny typ danych, który pozwala na przechowywanie wielu elementów w jednej zmiennej. 
# Elementy w liście mogą być dowolnego typu, a nawet mogą być różnych typów. Możesz tworzyć listy za pomocą nawiasów kwadratowych, a elementy w liście są oddzielane przecinkami.

# Na przykład:

numbers = [1, 2, 3, 4, 5]
words = ['cat', 'dog', 'bird']
mixed = [1, 'cat', 3.14, True]

#Powyższe przykłady tworzą trzy listy: "numbers", "words" i "mixed". 
# Lista "numbers" zawiera pięć liczb całkowitych, lista "words" zawiera trzy łańcuchy znaków, a lista "mixed" zawiera różne typy danych: liczbę całkowitą, łańcuch znaków i wartość logiczną.

# Możesz uzyskać dostęp do elementów listy za pomocą indeksów. 
# Indeksy są to liczby całkowite, które określają pozycję elementu w liście (liczone od zera). 
# Na przykład, jeśli chcesz uzyskać dostęp do drugiego elementu w liście "words", możesz użyć indeksu 1:

# second_word = words[1]  # second_word zostanie przypisane wartości 'dog'

# Możesz również użyć indeksów ujemnych, aby uzyskać dostęp do elementów listy od końca. 
# Na przykład, aby uzyskać dostęp do ostatniego elementu w liście "words", możesz użyć indeksu -1:

last_word = words[-1]  # last_word zostanie przypisane wartości 'bird'

# Możesz również użyć operatorów indeksowania i przeciążania, aby pobrać podlistę (tzw. "slicing"). 
# Na przykład, aby pobrać drugi i trzeci element z listy "numbers", możesz użyć następującego kodu:

sublist = numbers[1]
