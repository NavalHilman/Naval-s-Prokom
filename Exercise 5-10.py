current_users = ['Admin', 'Kenzo', 'Alea', 'Zahra', 'Arkana']
new_users = ['kenzo', 'Nayla', 'ALEA', 'Raffi', 'Queenza']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Yah username {new_user} udah dipakai orang. Coba pakai yang lain ya!")
    else:
        print(f"Asik username {new_user} masih available. Langsung pakai aja!")