# List tamu dari Exercise 3-6
guests = ["Zhafa", "Lou", "Nostradamus", "Marie Curie", "Alfie Williams", "Alain"]

# Kabar: tempat cuma cukup buat dua orang
print("Sori guys, ternyata gue cuma bisa ngundang dua orang aja nih.")

# Hapus tamu satu-satu pakai pop(), terus minta maaf
removed_guest = guests.pop()
print(f"\nSori {removed_guest}, lo belum bisa gue undang malem ini.")

removed_guest = guests.pop()
print(f"Sori {removed_guest}, lo belum bisa gue undang malem ini.")

removed_guest = guests.pop()
print(f"Sori {removed_guest}, lo belum bisa gue undang malem ini.")

removed_guest = guests.pop()
print(f"Sori {removed_guest}, lo belum bisa gue undang malem ini.")

# Dua orang yang masih ada di list tetap diundang
print(f"\nEh {guests[0]}, lo tetep diundang ya nanti malem!")
print(f"Eh {guests[1]}, lo tetep diundang ya nanti malem!")

# Hapus dua nama terakhir pakai del sampai list kosong
del guests[1]
del guests[0]

# Pastiin list-nya udah kosong
print(f"\nIsi list sekarang: {guests}")