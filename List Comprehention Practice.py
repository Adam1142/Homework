l = []
x = int(input("Enter a number: "))
for a in range(x):
    if (a%2 == 0):
        continue
    else:
        l.append(a)
print(l)

fruits = ["apple", "banana", "cherry", "date", "watermelon"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)