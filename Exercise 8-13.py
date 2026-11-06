def build_profile(first, last, **user_info):
    """Membuat dictionary berisi semua informasi tentang seorang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'kenzo', 'pratama',
    city='semarang',
    hobby='main gitar',
    favorite_food='nasi goreng',
)

print(my_profile)

print(f"\nKenalin aku {my_profile['first_name'].title()} {my_profile['last_name'].title()}.")
print(f"Aku tinggal di {my_profile['city'].title()}.")
print(f"Hobiku {my_profile['hobby']} dan makanan favoritku {my_profile['favorite_food']}.")