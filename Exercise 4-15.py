# Kelipatan 3 dari 3 sampai 30
threes = list(range(3, 31, 3))

print("Nih aku tampilin kelipatan 3 dari 3 sampai 30!\n")

for number in threes:
    print(number)

# Daftar 10 kubik pertama
cubes = []

for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

print("\nNih aku tampilin 10 kubik pertama!\n")

for cube in cubes:
    print(cube)

# Daftar pizza favorit
pizzas = ["pepperoni", "margherita", "napolitan"]
friend_pizzas = pizzas[:]

pizzas.append("hawaiian")
friend_pizzas.append("four cheese")

print("\nPizza favorit aku nih:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temen aku nih:")
for pizza in friend_pizzas:
    print(pizza)