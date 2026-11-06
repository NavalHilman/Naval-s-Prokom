cities = {
    'tokyo': {
        'country': 'jepang',
        'population': 14000000,
        'fact': 'punya penyeberangan Shibuya yang super rame banget.',
    },
    'jakarta': {
        'country': 'indonesia',
        'population': 10500000,
        'fact': 'jadi pusat bisnis dan ibu kota negara yang sibuk terus.',
    },
    'paris': {
        'country': 'prancis',
        'population': 2100000,
        'fact': 'terkenal sama Menara Eiffel yang ikonik itu.',
    },
}

for city, info in cities.items():
    print(f"\nKota {city.title()}:")
    print(f"- Negara: {info['country'].title()}")
    print(f"- Penduduk: sekitar {info['population']} orang")
    print(f"- Fakta seru: kota ini {info['fact']}")