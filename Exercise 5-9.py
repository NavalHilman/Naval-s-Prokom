usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin! Mau lihat laporan status hari ini nggak?")
        else:
            print(f"Halo {username.title()}! Makasih ya udah login lagi.")
else:
    print("Kita butuh nyari pengguna dulu nih!")