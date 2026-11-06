# Data yang dipakai untuk tes
car = 'subaru'
name = 'Rina'
age = 17
friends = ['Budi', 'Sari', 'Dewi']

# Kategori 1: kesetaraan dan ketidaksetaraan string
print("1a. Car == 'subaru' bener nggak? Tebakan aku True.")
print(car == 'subaru')
print("\n1b. Car == 'audi' bener nggak? Tebakan aku False.")
print(car == 'audi')
print("\n1c. Car != 'audi' bener nggak? Tebakan aku True.")
print(car != 'audi')
print("\n1d. Car != 'subaru' bener nggak? Tebakan aku False.")
print(car != 'subaru')

# Kategori 2: tes dengan method lower()
print("\n2a. Name.lower() == 'rina' bener nggak? Tebakan aku True.")
print(name.lower() == 'rina')
print("\n2b. Name.lower() == 'Rina' bener nggak? Tebakan aku False.")
print(name.lower() == 'Rina')

# Kategori 3: tes angka
print("\n3a. Age == 17 bener nggak? Tebakan aku True.")
print(age == 17)
print("\n3b. Age == 18 bener nggak? Tebakan aku False.")
print(age == 18)
print("\n3c. Age != 20 bener nggak? Tebakan aku True.")
print(age != 20)
print("\n3d. Age != 17 bener nggak? Tebakan aku False.")
print(age != 17)
print("\n3e. Age > 10 bener nggak? Tebakan aku True.")
print(age > 10)
print("\n3f. Age > 17 bener nggak? Tebakan aku False.")
print(age > 17)
print("\n3g. Age < 18 bener nggak? Tebakan aku True.")
print(age < 18)
print("\n3h. Age < 17 bener nggak? Tebakan aku False.")
print(age < 17)
print("\n3i. Age >= 17 bener nggak? Tebakan aku True.")
print(age >= 17)
print("\n3j. Age >= 18 bener nggak? Tebakan aku False.")
print(age >= 18)
print("\n3k. Age <= 17 bener nggak? Tebakan aku True.")
print(age <= 17)
print("\n3l. Age <= 16 bener nggak? Tebakan aku False.")
print(age <= 16)

# Kategori 4: keyword and dan or
print("\n4a. Age > 10 and age < 20 bener nggak? Tebakan aku True.")
print(age > 10 and age < 20)
print("\n4b. Age > 10 and age < 15 bener nggak? Tebakan aku False.")
print(age > 10 and age < 15)
print("\n4c. Age < 10 or age > 15 bener nggak? Tebakan aku True.")
print(age < 10 or age > 15)
print("\n4d. Age < 10 or age > 20 bener nggak? Tebakan aku False.")
print(age < 10 or age > 20)

# Kategori 5: item ada di dalam list
print("\n5a. 'Budi' in friends bener nggak? Tebakan aku True.")
print('Budi' in friends)
print("\n5b. 'Andi' in friends bener nggak? Tebakan aku False.")
print('Andi' in friends)

# Kategori 6: item tidak ada di dalam list
print("\n6a. 'Andi' not in friends bener nggak? Tebakan aku True.")
print('Andi' not in friends)
print("\n6b. 'Budi' not in friends bener nggak? Tebakan aku False.")
print('Budi' not in friends)