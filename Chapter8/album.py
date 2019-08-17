def make_album(artist_name, album_title, number_of_songs=''):
	if number_of_songs:
		album = f"{artist_name, album_title, number_of_songs}"
	else:	
		album = f"{artist_name, album_title}"
	return album.title()

full_info = make_album('The Choo', 'Horizons')
print(full_info)

full_info = make_album('Skoipy', 'Tax Returns')
print(full_info)

full_info = make_album('mathius', 'goes to eleven', '11')
print(full_info)