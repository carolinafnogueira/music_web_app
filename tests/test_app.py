from lib.database_connection import DatabaseConnection

'''
When I make a POST request to /albums
with title, release year, and artist id
as body parameters
I should get a 200 response with no response
'''

def test_create_album(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
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
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '\n'.join(['Album(1, Book of Sound, 2017, 1)'])

'''
When I make a GET request to /artists
I get a list with all the artists names
in the artists table
'''

def test_get_artists(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

'''
When I make a POST request to /artists
with name and genre as body parameters
I should get a 200 response
'''

def test_post_new_artist(db_connection, web_client):
    db_connection.seed('seeds/record_store.sql')
    post_response = web_client.post('/artists', data={
        'name': 'Wild nothing',
        'genre': 'Indie'
        })
    assert post_response.status_code == 200

    get_response = web_client.get('/artists')

    assert get_response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'
