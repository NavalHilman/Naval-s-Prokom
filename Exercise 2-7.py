# Simpan nama dengan whitespace di awal dan akhir
name = "\t\n Naval Hilman \t\n"

# Tampilkan dengan whitespace
print("Dengan whitespace:")
print(name)

# Tampilkan setelah whitespace dihapus
print("Hapus di kiri (lstrip):")
print(name.lstrip())

print("Hapus di kanan (rstrip):")
print(name.rstrip())

print("Hapus di kedua sisi (strip):")
print(name.strip())