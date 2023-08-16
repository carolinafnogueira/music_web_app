from lib.album import Album

'''
Constructs an Album object 
with title, release year, and 
artist_id
'''

def test_constructs_album():
    album = Album(4,'Title test', 2000, 3)
    assert album.id == 4
    assert album.title == 'Title test'
    assert album.release_year == 2000
    assert album.artist_id == 3

