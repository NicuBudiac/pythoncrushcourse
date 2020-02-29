def make_album(artist_name,album_title,number_of_tracks = ''):
    album = {'artist ': artist_name , 'album' : album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks
    return album
    
musician = make_album('pink','in the world',number_of_tracks=10)
print(mus\