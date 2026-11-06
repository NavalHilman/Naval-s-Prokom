# Daftar negara yang ingin dikunjungi
countries = ["Jepang", "Italia", "Brasil", "Mesir"]
print(f"Daftar awal: {countries}")

# Mengakses elemen lewat indeks
print(f"Elemen pertama: {countries[0]}")

# Mengubah elemen
countries[1] = "Spanyol"
print(f"Setelah elemen kedua diubah: {countries}")

# append(): menambah di akhir list
countries.append("Kanada")
print(f"Setelah append(): {countries}")

# insert(): menyisipkan di posisi tertentu
countries.insert(2, "Norwegia")
print(f"Setelah insert(): {countries}")

# del: menghapus berdasarkan indeks
del countries[0]
print(f"Setelah del: {countries}")

# pop(): menghapus elemen terakhir dan menyimpannya
popped_country = countries.pop()
print(f"Setelah pop(): {countries} (yang dihapus: {popped_country})")

# remove(): menghapus berdasarkan nilai
countries.remove("Mesir")
print(f"Setelah remove(): {countries}")

# sorted(): urutan sementara, list asli tidak berubah
print(f"sorted(): {sorted(countries)}")
print(f"List asli: {countries}")

# sort(): mengurutkan list secara permanen
countries.sort()
print(f"Setelah sort(): {countries}")

# reverse(): membalik urutan list
countries.reverse()
print(f"Setelah reverse(): {countries}")

# len(): menghitung jumlah elemen
print(f"Jumlah negara di list: {len(countries)}")