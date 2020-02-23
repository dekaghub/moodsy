import os, io
from google.cloud import vision
from flask import redirect, render_template

def process_image(filepath):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service-account-token.json'

    client = vision.ImageAnnotatorClient()

    # image file
    image_location = filepath

    with io.open(image_location, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content = content)

    response = client.face_detection(image = image)
    faces = response.face_annotations

    # Google's definition
    # likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')

    # Numerical definition for calc
    likelihood_name = (-1,1,2,3,4,5)

    emotions = {'joy' : [],
                'anger' : [],
                'sorrow' : [],
                'surprise' : []
                }

    for face in faces:
        emotions['joy'].append(likelihood_name[face.joy_likelihood])
        emotions['anger'].append(likelihood_name[face.anger_likelihood])
        emotions['sorrow'].append(likelihood_name[face.sorrow_likelihood])
        emotions['surprise'].append(likelihood_name[face.surprise_likelihood])

    
    return render_template('test.html', value=faces)