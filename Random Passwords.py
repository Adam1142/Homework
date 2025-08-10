import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
l = int(input("Enter password length: "))
password = ""
for a in range(l):
    password += random.choice(Chars)
print("Your new password is:", password)