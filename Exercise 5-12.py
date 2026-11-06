# 5-7
favorite_fruits = ['mangga', 'durian', 'apel']

if 'mangga' in favorite_fruits:
    print("Kamu emang suka banget sama mangga ya!")

# 5-8 dan 5-9
usernames = ['admin', 'kenzo', 'alea', 'zahra', 'arkana']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin! Mau lihat laporan status hari ini nggak?")
        else:
            print(f"Halo {username.title()}! Makasih ya udah login lagi.")
else:
    print("Kita butuh nyari pengguna dulu nih!")

# 5-10
current_users_lower = [user.lower() for user in ['Admin', 'Kenzo', 'Alea']]

if 'kenzo' in current_users_lower:
    print("Yah username udah dipakai orang. Coba pakai yang lain ya!")

# 5-11
for number in range(1, 10):
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")