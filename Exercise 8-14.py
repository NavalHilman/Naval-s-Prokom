def make_car(manufacturer, model, **car_info):
    """Menyimpan informasi mobil di dalam sebuah dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

print(f"\nMobil ini {car['manufacturer'].title()} {car['model'].title()} warna {car['color']}.")
print("Katanya sih udah lengkap sama tow package. Mantap buat petualangan!")