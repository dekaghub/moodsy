import sys
import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# sp.trace = False

from spotipy.oauth2 import SpotifyClientCredentials

# testing
clientID = '5e3b1a5db9854632bf9207c20eb44424'
clientSecret = '0c093a2a8bb24aa8bee9b5ff36866cc5'

client_creds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_creds)

def songReco(artistIDs):
    results = sp.recommendations(limit=3,
                                seed_artists=artistIDs,
                                target_energy=.5,
                                target_danceability=.7)
    # for track in results:
    #     print(track['name'], '-', track['artists'][0]['name'])
    return results


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    for track in results['tracks']:
        print(track['name'], '-', track['artists'][0]['name'])


if __name__ == '__main__':
    
    names = ['Prunk', 'El Funkador', 'Prodot']
    uri_ids = []

    for name in names:
        result = get_artist(name)
        uri_ids.append(result['id'])

    tmp = songReco(uri_ids)
    
    for track in tmp['tracks']:
        print(track['artists'][0]['name'], ' - ', track['name'], '\n\t ', 'Spotify : ', track['external_urls']['spotify'])

    # for t in tmp:    
    #     print(t['tracks'][0]['external_urls']['spotify'])
    #     print(t['tracks'][0]['artists'][0]['name'])
    #     print(t['tracks'][0]['name'])

