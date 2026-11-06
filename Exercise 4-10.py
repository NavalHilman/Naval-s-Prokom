# Buat list 10 kubik pertama dengan list comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(f"Isi list lengkap: {cubes}\n")

# Tiga item pertama
print("Tiga item pertama di list ini adalah:")
print(cubes[:3])

# Tiga item dari tengah
print("\nTiga item dari tengah list ini adalah:")
print(cubes[3:6])

# Tiga item terakhir
print("\nTiga item terakhir di list ini adalah:")
print(cubes[-3:])