pet_1 = {
    'animal': 'kucing',
    'owner': 'Kenzo',
}

pet_2 = {
    'animal': 'anjing',
    'owner': 'Alea',
}

pet_3 = {
    'animal': 'kelinci',
    'owner': 'Zahra',
}

pet_4 = {
    'animal': 'hamster',
    'owner': 'Arkana',
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Ada {pet['animal']} lucu punya {pet['owner']}.")
    print(f"Jenis hewannya: {pet['animal']}")
    print(f"Pemiliknya: {pet['owner']}\n")