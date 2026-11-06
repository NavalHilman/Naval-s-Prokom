# Daftar tempat yang ingin dikunjungi (sengaja tidak berurutan abjad)
places = ["Lake Como", "Rome", "New York", "Tokyo", "Shibuya"]

# 1. Tampilkan urutan asli
print("Urutan asli:")
print(places)

# 2. sorted() mengurutkan abjad tanpa mengubah list asli
print("\nsorted() urut abjad:")
print(sorted(places))

# 3. Tampilkan list asli untuk membuktikan urutannya tidak berubah
print("\nList asli (belum berubah):")
print(places)

# 4. sorted() dengan urutan abjad terbalik, list asli tetap sama
print("\nsorted() abjad terbalik:")
print(sorted(places, reverse=True))

# 5. Tampilkan list asli sekali lagi
print("\nList asli (belum berubah):")
print(places)

# 6. reverse() membalik urutan list secara permanen
places.reverse()
print("\nSetelah reverse():")
print(places)

# 7. reverse() lagi, urutan kembali seperti semula
places.reverse()
print("\nSetelah reverse() lagi:")
print(places)

# 8. sort() mengurutkan list berdasarkan abjad secara permanen
places.sort()
print("\nSetelah sort():")
print(places)

# 9. sort() dengan urutan abjad terbalik secara permanen
places.sort(reverse=True)
print("\nSetelah sort(reverse=True):")
print(places)