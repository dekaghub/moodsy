import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)


# To gain access to user's personal information, you need to use the old school util method (requires verifying of redirect URL):

import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(
        username=your_username,
        scope=scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)

spotify = spotipy.Spotify(auth=token)



# get artist reco

import sys
import spotipy

''' shows recommendations for the given artist
'''

from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


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
    if len(sys.argv) < 2:
        print(('Usage: {0} artist name'.format(sys.argv[0])))
    else:
        name = ' '.join(sys.argv[1:])
        artist = get_artist(name)
        if artist:
            show_recommendations_for_artist(artist)
        else:
            print("Can't find that artist", name)