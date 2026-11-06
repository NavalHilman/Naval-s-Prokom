def city_country(city, country):
    """Mengembalikan string berformat 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"


result_1 = city_country('semarang', 'indonesia')
result_2 = city_country('tokyo', 'jepang')
result_3 = city_country('paris', 'prancis')

print(result_1)
print(result_2)
print(result_3)