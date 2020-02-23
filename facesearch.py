import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service-account-token.json'

client = vision.ImageAnnotatorClient()

# image file
image_location = 'sad.jpeg'

with io.open(image_location, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content = content)

response = client.face_detection(image = image)
faces = response.face_annotations

# Google's definition
# likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')

# Numerical definition for calc
likelihood_name = (-1,1,2,3,4,5)

num_faces = len(faces)

emotions = {'joy' : [],
            'anger' : [],
            'sorrow' : [],
            'surprise' : []
            }

if num_faces > 1:

    for face in faces:
        print(' in faces 3')
        emotions['joy'].append(likelihood_name[face.joy_likelihood])
        emotions['anger'].append(likelihood_name[face.anger_likelihood])
        emotions['sorrow'].append(likelihood_name[face.sorrow_likelihood])
        emotions['surprise'].append(likelihood_name[face.surprise_likelihood])

    joy = sum(emotions['joy'])/len(emotions['joy'])
    anger = sum(emotions['anger'])/len(emotions['anger'])
    sorrow = sum(emotions['sorrow'])/len(emotions['sorrow'])
    surprise = sum(emotions['surprise'])/len(emotions['surprise'])

    emotions = {'joy' : joy,
            'anger' : anger,
            'sorrow' : sorrow,
            'surprise' : surprise
            }
elif num_faces == 1:
    print(' in faces 1')
    emotions = {'joy' : likelihood_name[faces[0].joy_likelihood],
            'anger' : likelihood_name[faces[0].anger_likelihood],
            'sorrow' : likelihood_name[faces[0].sorrow_likelihood],
            'surprise' : likelihood_name[faces[0].surprise_likelihood]
            }

print(emotions)