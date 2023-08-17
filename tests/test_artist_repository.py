from lib.artist_repository import ArtistRepository
from lib.artist import Artist

'''
When I call ArtistRepository #all
I get a list of all the artists objects
in the artists table
'''

def test_get_artists_names(db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = ArtistRepository(db_connection)
    artists = repository.all()
    assert artists == ['Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone']
    
   