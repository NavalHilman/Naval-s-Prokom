# Daftar pizza favorit dari Exercise 4-1
pizzas = ["pepperoni", "margherita", "napolitan"]

# Salin list pizzas ke friend_pizzas menggunakan slice
friend_pizzas = pizzas[:]

# Tambahkan pizza baru ke list asli
pizzas.append("hawaiian")

# Tambahkan pizza yang berbeda ke list teman
friend_pizzas.append("four cheese")

# Tampilkan pizza favorit milikku
print("Pizza favorit aku nih:")
for pizza in pizzas:
    print(pizza)

# Tampilkan pizza favorit milik temanku
print("\nPizza favorit temen aku nih:")
for pizza in friend_pizzas:
    print(pizza)