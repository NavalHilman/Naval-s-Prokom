# List tamu dari Exercise 3-4
guests = ["Nikola Tesla", "Marie Curie", "Alfie Williams"]

# Undangan pertama
print(f"Halo {guests[0]}, maukah kamu datang ke rumahku?")
print(f"Halo {guests[1]}, datangkah dikau nanti ke rumah kanda?")
print(f"Halo {guests[2]}, lu dateng ga nanti malam?")

# Salah satu tamu tidak bisa datang
print(f"\n{guests[0]} tidak dapat hadir.")

# Ganti tamu yang tidak bisa datang dengan tamu baru
guests[0] = "Lou"

# Undangan kedua untuk semua orang yang ada di list sekarang
print(f"\nHalo {guests[0]}, nanti malam bisa datang kan?")
print(f"Halo {guests[1]}, datangkah dikau nanti ke rumah kanda?")
print(f"Halo {guests[2]}, lu dateng ga nanti malam?") 