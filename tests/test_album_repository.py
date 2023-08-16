from lib.album_repository import AlbumRepository
from lib.album import Album

'''
When we call the method #all,
we receive a list with all the
albums in the albums list in a 
human readable format
'''

def test_list_all_albums(db_connection):
    db_connection.seed('seeds/albums.sql')
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Book of Sound', 2017, 1)
    ]


'''
When we call the method #add_album, we have a new
album added to the database
'''

def test_add_album_to_music_library(db_connection):
    db_connection.seed('seeds/albums.sql')
    repository = AlbumRepository(db_connection)
    repository.add_album(Album(None, 'test title', 1780, 2))
    assert repository.all() == [
        Album(1, 'Book of Sound', 2017, 1),
        Album(2, 'test title', 1780, 2)
    ]


    