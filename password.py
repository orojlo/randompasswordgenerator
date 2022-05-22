from operator import length_hint
import random

print("Simple Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=,.?0123456789'


number = input('Amount Of Password To generate : ')

number = int(number)

length = input('How many passowrd lenght ? : ')
length = int(length)


print("\nYour Passwors:")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)