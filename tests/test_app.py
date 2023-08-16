from lib.database_connection import DatabaseConnection

'''
When I make a POST request to /albums
with title, release year, and artist id
as body parameters
I should get a 200 response with no response
'''

def test_create_album(db_connection, web_client):
    db_connection.seed('seeds/albums.sql')
    response = web_client.post('/albums', data={
        'title': 'Test title', 
        'release_year': '1900', 
        'artist_id': '3'
        })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

'''
When I make a GET request to /albums
I get a list with all the albums 
in the albums table
'''

def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/albums.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '\n'.join(['Album(1, Book of Sound, 2017, 1)'])