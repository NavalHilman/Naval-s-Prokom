usernames = ['admin', 'kenzo', 'alea', 'zahra', 'arkana']

for username in usernames:
    if username == 'admin':
        print("Halo admin! Mau lihat laporan status hari ini nggak?")
    else:
        print(f"Halo {username.title()}! Makasih ya udah login lagi.")