# Daftar makanan favorit
my_foods = ['pizza', 'falafel', 'carrot cake']

# Salin list my_foods ke friend_foods
friend_foods = my_foods[:]

# Tambahkan makanan berbeda ke masing-masing list
my_foods.append('cannoli')
friend_foods.append('ice cream')

# Tampilkan makanan favoritku dengan for loop
print("Makanan favorit aku nih:")
for food in my_foods:
    print(food)

# Tampilkan makanan favorit temanku dengan for loop
print("\nMakanan favorit temen aku nih:")
for food in friend_foods:
    print(food)