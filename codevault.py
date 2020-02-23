
# Math Functions
import math

# Sigmoid
def sigmoid(x):
    return 1/(1 + math.exp(-x))

# softmax
def softmax(x):
    return x/(math.fabs(x) + 1)

# tanh
math.tanh(x)

# linear


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


# code dump
joy = jassObject['joy']
anger = jassObject['anger']
sorrow = jassObject['sorrow']
surprise = jassObject['surprise']


# old number map
import random as r
import math

# start of mapping vision to spotify

# joy = anger = sadness = sorrow = 0

# energy = danceability = valence = 0

# acoustic = liveness = 0

# Sigmoid
def sigmoid(x):
    return 1/(1 + math.exp(-x))

# softmax
def softmax(x):
    return x/(math.fabs(x) + 1)

emotions = {'joy' : 0,
            'anger' : 0,
            'sorrow' : 0,
            'surprise' : 0
            }


# return tag for low energy, neutral, upbeat, ambivalent
def mood_spectrum(jassObject):
    if jassObject['joy'] > 3 and jassObject['sorrow'] < 3:
        return 'upbeat'
    if jassObject['sorrow'] > 2 or jassObject['joy'] < 4:
        return 'neutral'
    if jassObject['anger'] > 3 or jassObject['joy'] > 3:
        return 'phase'
    else:
        return 'ambivalent'

# mood factor -- multiplier for spotify levels  (0 - 1); 1 = positive
def mood_factor(tag):
    if tag == 'upbeat':
        return 0.5
    if tag == 'neutral':
        return (.01 * r.randint(0,10))
    if tag == 'phase':
        return (.0069 * r.randint(1,5))
    if tag == 'ambivalent':
        return (.00042069 * r.randint(1,69))

# direct multipliers
def spotifySliders(jassObject):
    joy, anger, sorrow, surprise = jassObject.values()
    trackParameters = { 'danceability' : 0,
                    'energy' : 0,
                    'valence' : 0,
                    'acoustic' : 0,
                    'liveness' : 0
}

    mFactor = mood_factor(mood_spectrum(jassObject)) * r.randint(-1,1)

    trackParameters['danceability'] = (math.fabs(math.fabs(mFactor) * joy/5 + (1/sorrow) * sigmoid(joy)/softmax(joy)))
    
    trackParameters['energy'] = (0.8 * joy/5 + mFactor * (anger/joy)) * .75

    trackParameters['valence'] = 1 - sorrow/5 + (sigmoid(sorrow) * mFactor) + (1/joy) * softmax(sorrow)

    trackParameters['acoustic'] = sorrow/5 + .2 * joy/5

    trackParameters['liveness'] = 0.25 * r.randint(0,1) + sorrow/joy * softmax(r.randint(1,3)) + anger * mFactor * 0.3

    return trackParameters


if __name__ == '__main__':

    emotions = {'joy' : 0,
            'anger' : 0,
            'sorrow' : 0,
            'surprise' : 0
            }
    
    for i in range(10):
        emotions['joy'] = r.choice([-1,1,2,3,4,5])
        emotions['anger'] = r.choice([-1,1,2,3,4,5])
        emotions['sorrow'] = r.choice([-1,1,2,3,4,5])
        emotions['surprise'] = r.choice([-1,1,2,3,4,5])

        spotifyObj = spotifySliders(emotions)

        print(emotions)
        print(spotifyObj)


# Honky Ponky working kowde
import random as r
import math

# Sigmoid
def sigmoid(x):
    return 1/(1 + math.exp(-x))

# softmax
def softmax(x):
    return x/(math.fabs(x) + 1)

emotions = {'joy' : 0,
            'anger' : 0,
            'sorrow' : 0,
            'surprise' : 0
            }


# return tag for low energy, neutral, upbeat, ambivalent
def mood_spectrum(jassObject):
    if jassObject['joy'] > 3 and jassObject['sorrow'] < 3:
        return 'upbeat'
    if jassObject['sorrow'] > 2 or jassObject['joy'] < 4:
        return 'neutral'
    if jassObject['anger'] > 3 or jassObject['joy'] > 3:
        return 'phase'
    else:
        return 'ambivalent'

# mood factor -- multiplier for spotify levels  (0 - 1); 1 = positive
def mood_factor(tag):
    if tag == 'upbeat':
        return 0.5
    if tag == 'neutral':
        return (.01 * r.randint(0,10))
    if tag == 'phase':
        return (.0069 * r.randint(1,5))
    if tag == 'ambivalent':
        return (.00042069 * r.randint(1,69))

# direct multipliers
def spotifySliders(jassObject):
    joy, anger, sorrow, surprise = jassObject.values()
    trackParameters = { 'danceability' : 0,
                    'energy' : 0,
                    'valence' : 0,
                    'acoustic' : 0,
                    'liveness' : 0
}

    mFactor = mood_factor(mood_spectrum(jassObject)) * r.randint(-1,1)
    print('mFactor : ', mFactor)
    trackParameters['danceability'] = r.uniform(sigmoid(joy/5 + softmax(anger * mFactor)), .9) + mFactor * 1/sorrow * 0.5
    
    trackParameters['energy'] = math.fabs(r.uniform((0.8 * (joy/5 + anger/5) + mFactor * (anger/joy)) * .7, .99))

    trackParameters['valence'] = math.fabs(((sorrow/5) * .5) + ((1/joy) * .3) + r.uniform(softmax(anger), 1) * mFactor)
    trackParameters['acoustic'] = r.uniform((math.fabs(sorrow/5 + .2 * joy/5)* 0.75), .9)

    trackParameters['liveness'] = r.uniform(math.fabs(softmax(sorrow)), .8) + mFactor * r.uniform(sigmoid(joy) * 0.4, .7)

    return trackParameters


if __name__ == '__main__':

    emotions = {'joy' : 0,
            'anger' : 0,
            'sorrow' : 0,
            'surprise' : 0
            }
    
    for i in range(10):
        emotions['joy'] = r.choice([-1,1,2,3,4,5])
        emotions['anger'] = r.choice([-1,1,2,3,4,5])
        emotions['sorrow'] = r.choice([-1,1,2,3,4,5])
        emotions['surprise'] = r.choice([-1,1,2,3,4,5])

        spotifyObj = spotifySliders(emotions)

        print(emotions)
        print(spotifyObj)