favorite_numbers = {
    'kenzo': [7, 21],
    'alea': [14, 3, 9],
    'zahra': [3, 8],
    'arkana': [21, 5, 11],
    'nayla': [9],
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(f"- {number} (angka andalan nih!)") 