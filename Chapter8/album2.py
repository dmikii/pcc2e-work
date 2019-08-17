def make_album(artist_name, album_title):
	album = f"{artist_name}, {album_title}"
	return album.title()

while True:
	print("\nTell me the artist name and album title: ")
	print("(enter 'q' at any time to quit)")
	
	artist = input("Artist: ")
	if artist == 'q':
		break
	title = input("Album: ")
	if title == 'q':
		break

	final_info = make_album(artist, title)
	print(f"\nThe album is {final_info}.")
