favorite_places = {
    'kenzo': ['Bali', 'Yogyakarta', 'Bromo'],
    'alea': ['Bandung', 'Labuan Bajo'],
    'zahra': ['Raja Ampat'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place} (seru banget buat dikunjungi!)")