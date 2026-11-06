# Daftar tamu awal (tiga orang)
guests = ["Lou", "Marie Curie", "Alfie Williams"]

# Kabar: diminta mengundang lebih banyak orang
print("Orangtuaku menyuruhku untuk mengundang lebih banyak orang!")

# Tambah satu tamu di awal list
guests.insert(0, "Zhafa")

# Tambah satu tamu di tengah list
guests.insert(2, "Nostradamus")

# Tambah satu tamu di akhir list
guests.append("Alain")

# Tampilkan undangan untuk semua tamu
print(f"\nHalo {guests[0]}, nanti malam bisa datang kan?")
print(f"Halo {guests[1]}, nanti malam bisa datang kan?")
print(f"Halo {guests[2]}, nanti malam bisa datang kan?")
print(f"Halo {guests[3]}, nanti malam bisa datang kan?")
print(f"Halo {guests[4]}, nanti malam bisa datang kan?")
print(f"Halo {guests[5]}, nanti malam bisa datang kan?")

# Hitung jumlah tamu dengan len(), lalu tampilkan
print(f"\nJumlah orang yang aku undang makan malam: {len(guests)}")