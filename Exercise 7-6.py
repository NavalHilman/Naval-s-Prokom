prompt = "\nTopping apa yang mau ditambahin ke pizza kamu?"
prompt += "\nKetik 'quit' kalau udah cukup: "

# Versi 1: kondisi di dalam while
topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Oke siap! Topping {topping} bakal kami tambahin ke pizza kamu.")

# Versi 2: variabel aktif
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Oke siap! Topping {topping} bakal kami tambahin ke pizza kamu.")

# Versi 3: pernyataan break
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Oke siap! Topping {topping} bakal kami tambahin ke pizza kamu.")