def make_album(artist_name,album_title,number_of_tracks = ''):
    album = {'artist ': artist_name , 'album' : album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks
    return album
while True:
    print("\nTell me your name")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name :")
    if artist_name == 'q':
        break
    album_title = input ("Album title:")
    if album_title == 'q':
        break
format_name = make_album(artist_name,album_title)
print(format_name)
