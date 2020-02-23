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
    trackParameters['danceability'] = sigmoid(joy/5 + anger/5) * 0.8 + softmax(joy/anger) * math.tanh(joy/anger) *  1/sorrow * mFactor
    
    trackParameters['energy'] = math.fabs((0.8 * (joy/5 + anger/5) + mFactor * (anger/joy)) * .75)

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

