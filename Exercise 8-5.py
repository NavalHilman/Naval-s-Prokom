def describe_city(city, country='Indonesia'):
    """Menampilkan kalimat sederhana tentang sebuah kota dan negaranya."""
    print(f"{city.title()} itu ada di {country.title()} lho. Pernah main ke sana belum?")


describe_city('semarang')
describe_city('bandung')
describe_city('tokyo', 'jepang')