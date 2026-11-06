sandwich_orders = ['tuna', 'ayam crispy', 'telur', 'keju']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Sandwich {current_sandwich} udah jadi nih. Silakan diambil ya!")
    finished_sandwiches.append(current_sandwich)

print("\nSemua sandwich yang udah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")