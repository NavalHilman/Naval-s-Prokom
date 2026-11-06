favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['jen', 'kenzo', 'edward', 'alea', 'phil', 'zahra']

for person in people:
    if person in favorite_languages.keys():
        print(f"Makasih ya {person.title()} udah mau ikut polling!")
    else:
        print(f"Hai {person.title()}! Yuk ikutan polling bahasa favorit kita!")