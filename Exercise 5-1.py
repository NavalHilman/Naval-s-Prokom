# Data yang dipakai untuk tes
car = 'subaru'
name = 'Rina'
age = 17
friends = ['Budi', 'Sari', 'Dewi']

# Tes 1: sama dengan (True)
print("Eh car == 'subaru' bener nggak ya? Tebakan aku True.")
print(car == 'subaru')

# Tes 2: sama dengan (False)
print("\nTerus car == 'audi' bener nggak? Tebakan aku False.")
print(car == 'audi')

# Tes 3: tidak sama dengan (True)
print("\nKalau car != 'audi' gimana? Tebakan aku True.")
print(car != 'audi')

# Tes 4: huruf besar dan kecil dianggap beda (False)
print("\nName == 'rina' padahal isinya 'Rina'? Tebakan aku False.")
print(name == 'rina')

# Tes 5: memakai lower() (True)
print("\nKalau pakai name.lower() == 'rina' hasilnya? Tebakan aku True.")
print(name.lower() == 'rina')

# Tes 6: lebih besar atau sama dengan (False)
print("\nUmur aku udah 18 ke atas belum? Tebakan aku False.")
print(age >= 18)

# Tes 7: lebih kecil (True)
print("\nUmur aku di bawah 18 nggak? Tebakan aku True.")
print(age < 18)

# Tes 8: operator and (True)
print("\nUmur aku di antara 10 dan 20 kan? Tebakan aku True.")
print(age > 10 and age < 20)

# Tes 9: operator or (False)
print("\nUmur aku di bawah 10 atau di atas 20? Tebakan aku False.")
print(age < 10 or age > 20)

# Tes 10: mengecek isi list dengan in (False)
print("\nAndi ada di daftar temen aku nggak? Tebakan aku False.")
print('Andi' in friends)