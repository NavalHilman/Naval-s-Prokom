prompt = "\nBerapa umur kamu?"
prompt += "\nKetik 'quit' kalau mau udahan: "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Yeay tiket kamu gratis! Selamat nonton ya!")
    elif age <= 12:
        print("Tiket kamu $10 aja nih. Jangan lupa beli popcorn!")
    else:
        print("Tiket kamu $15 ya. Siap-siap seru-seruan di bioskop!")