sandwich_orders = [
    'pastrami', 'tuna', 'pastrami', 'ayam crispy',
    'telur', 'pastrami', 'keju',
]
finished_sandwiches = []

print("Maaf ya pastrami-nya lagi abis nih. Pesanan pastrami kami batalin dulu.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Sandwich {current_sandwich} udah jadi nih. Silakan diambil ya!")
    finished_sandwiches.append(current_sandwich)

print("\nSemua sandwich yang udah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")