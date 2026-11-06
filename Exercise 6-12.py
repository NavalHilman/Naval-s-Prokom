cities = {
    'tokyo': {
        'country': 'jepang',
        'population': 14000000,
        'language': 'bahasa Jepang',
        'landmarks': ['Tokyo Tower', 'Senso-ji', 'Shibuya Crossing'],
        'fact': 'punya penyeberangan Shibuya yang super rame banget.',
    },
    'jakarta': {
        'country': 'indonesia',
        'population': 10500000,
        'language': 'bahasa Indonesia',
        'landmarks': ['Monas', 'Kota Tua'],
        'fact': 'jadi pusat bisnis dan ibu kota negara yang sibuk terus.',
    },
    'paris': {
        'country': 'prancis',
        'population': 2100000,
        'language': 'bahasa Prancis',
        'landmarks': ['Menara Eiffel', 'Museum Louvre', 'Notre-Dame'],
        'fact': 'terkenal sama Menara Eiffel yang ikonik itu.',
    },
}

for city, info in cities.items():
    print(f"\n=== Kota {city.title()} ===")
    print(f"Negara     : {info['country'].title()}")
    print(f"Penduduk   : sekitar {info['population']:,} orang")
    print(f"Bahasa     : {info['language']}")
    print(f"Fakta seru : kota ini {info['fact']}")
    print("Tempat yang wajib dikunjungi:")
    for landmark in info['landmarks']:
        print(f"  * {landmark} (jangan lupa foto-foto ya!)")