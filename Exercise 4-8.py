# Buat list kosong untuk menyimpan kubik
cubes = []

# Hitung kubik dari 1 sampai 10 lalu masukkan ke dalam list
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

# Pesan pembuka
print("Nih aku tampilin 10 kubik pertama!\n")

# Tampilkan setiap kubik
for cube in cubes:
    print(cube)