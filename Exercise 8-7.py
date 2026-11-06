def make_album(artist, title, tracks=None):
    """Membuat dictionary yang menggambarkan sebuah album musik."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


album_1 = make_album('Tulus', 'Manusia')
album_2 = make_album('Hindia', 'Menari dengan Bayangan')
album_3 = make_album('Raisa', 'Handmade', tracks=11)

print("Album pertama yang masuk playlist:")
print(album_1)
print("\nAlbum kedua yang nggak kalah asik:")
print(album_2)
print("\nAlbum ketiga lengkap sama jumlah lagunya:")
print(album_3)