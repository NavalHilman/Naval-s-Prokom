def make_album(artist, title, tracks=None):
    """Membuat dictionary yang menggambarkan sebuah album musik."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print("\nYuk masukin data album favorit kamu!")
    print("(Ketik 'q' kapan aja kalau mau udahan)")

    artist = input("Nama artisnya siapa? ")
    if artist == 'q':
        break

    title = input("Judul albumnya apa? ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(f"Mantap! Album yang udah kamu catat: {album}")

print("\nMakasih ya udah berbagi selera musik kamu!")