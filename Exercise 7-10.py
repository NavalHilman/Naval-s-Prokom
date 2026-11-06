responses = {}

polling_active = True

while polling_active:
    name = input("\nNama kamu siapa nih? ")
    place = input("Kalau bisa liburan ke satu tempat di dunia kamu pilih ke mana? ")

    responses[name] = place

    repeat = input("Masih ada orang lain yang mau ikut polling? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Hasil Polling Liburan Impian ---")
for name, place in responses.items():
    print(f"{name.title()} pengin banget liburan ke {place.title()}!")