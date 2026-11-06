rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"Sungai {river.title()} ngalir lewat {country.title()} lho.")

print("\nDaftar sungai yang udah dicatat:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nDaftar negara yang dilewati sungai:")
for country in rivers.values():
    print(f"- {country.title()}")