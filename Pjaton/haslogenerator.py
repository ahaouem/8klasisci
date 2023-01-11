import string
import random

# Funkcja do generowania hasła
def generate_password(length, digits, upper, lower):
    password = ""
    chars = ""
    if digits:
        chars += string.digits
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase
    for i in range(length):
        password += random.choice(chars)
    return password

# Ustawienia kryteriów bezpieczeństwa hasła
password_length = 16
password_digits = True
password_upper = True
password_lower = True

# Wygenerowanie hasła
password = generate_password(password_length, password_digits, password_upper, password_lower)
print("Wygenerowane hasło: ", password)

# Zapis hasła do pliku
with open('passwords.txt', 'a') as f:
    f.write(password+"\n")

