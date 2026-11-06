person_1 = {
    'first_name': 'Kenzo',
    'last_name': 'Pratama',
    'age': 22,
    'city': 'Semarang',
}

person_2 = {
    'first_name': 'Alea',
    'last_name': 'Putri',
    'age': 20,
    'city': 'Bandung',
}

person_3 = {
    'first_name': 'Arkana',
    'last_name': 'Wijaya',
    'age': 24,
    'city': 'Surabaya',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Kenalin nih {full_name}.")
    print(f"Umurnya {person['age']} tahun lho.")
    print(f"Dia tinggal di {person['city']}.\n")