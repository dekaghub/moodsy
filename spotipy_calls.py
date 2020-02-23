import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random as r

import number_maps as googleToSpotify

# testing
clientID = '5e3b1a5db9854632bf9207c20eb44424'
clientSecret = '0c093a2a8bb24aa8bee9b5ff36866cc5'

client_creds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_creds)

recoObj = googleToSpotify.spotifySliders(emotions)

def songReco(artistObj, recoObj):
    results = sp.recommendations(limit=3,
                                seed_artists=artistObj,
                                min_danceability=float("{0:.2f}".format(r.uniform(recoObj['danceability'] * .5, recoObj['danceability']))),
                                max_danceability=float("{0:.2f}".format(r.uniform(recoObj['danceability'] * .8, .9))),
                                min_energy=float("{0:.2f}".format(r.uniform(recoObj['energy'] * .6, recoObj['energy']))),
                                max_energy=float("{0:.2f}".format(r.uniform(recoObj['energy'] * .8, .9))),
                                min_valence=float("{0:.2f}".format(r.uniform(recoObj['valence'] * .6, recoObj['valence']))),
                                max_valence=float("{0:.2f}".format(r.uniform(recoObj['valence'] * .8, .9))),
                                min_acoustic=float("{0:.2f}".format(r.uniform(recoObj['acoustic'] * .6, recoObj['acoustic']))),
                                max_acoustic=float("{0:.2f}".format(r.uniform(recoObj['acoustic'] * .8, .9))),
                                min_liveliness=float("{0:.2f}".format(r.uniform(recoObj['liveness'] * .6, recoObj['liveness']))),
                                max_liveliness=float("{0:.2f}".format(r.uniform(recoObj['liveness'] * .8, .9)))
                                )
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
    
    names = ['Prunk', 'Drake', 'Paramore', 'Kartell', 'Linkin Park', 'Mac Miller', 'Darius', 'Moon Boots', 'Claire', 'KAYTRANADA', 'Smino', 'Joe Hertz', 'Cheekface', 'Still Woozy', 'Talking Heads', 'Chvrches']
    uri_ids = []

    for i in range(2):
        result = get_artist(r.choice(names))
        uri_ids.append(result['id'])
    
    # print('Uri Ids : ', uri_ids)

    tmp = songReco(uri_ids, recoObj)
    
    for track in tmp['tracks']:
        print(track['artists'][0]['name'], ' - ', track['name'], '\n\t ', 'Spotify : ', track['external_urls']['spotify'])


