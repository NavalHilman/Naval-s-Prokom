prompt = "\nTopping apa yang mau ditambahin ke pizza kamu?"
prompt += "\nKetik 'quit' kalau udah cukup: "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Oke siap! Topping {topping} bakal kami tambahin ke pizza kamu.")