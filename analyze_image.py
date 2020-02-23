import os, io
from google.cloud import vision
from flask import redirect, render_template

def facesearch(filepath):

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

    # hasface = False

    # for face in faces:
    #     if emotions['joy'] != []:
    #         hasface = True
    #         break
    #     elif emotions['anger'] != []:
    #         hasface = True
    #         break
    #     elif emotions['sorrow'] != []:
    #         hasface = True
    #         break
    #     elif emotions['surprise'] != []:
    #         hasface = True

    # if hasface == False:
    #     colorsearch(filepath)
    # else:
    #     return render_template('test.html', value=emotions)
    return render_template('test.html', value=emotions)

# def colorsearch(filepath):

#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service-account-token.json'
    
#     client = vision.ImageAnnotatorClient()

#     with io.open(filepath, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.types.Image(content=content)

#     response = client.image_properties(image=image)
#     props = response.image_properties_annotation

    # colors = {'fraction': [], 
    #             'red' : [],
    #             'green' : [],
    #             'blue' : [],
    #             'opacity' : []
    #             }

    # for color in props.dominant_colors.colors:
    #     colors['fraction'].append('fraction: {}'.format(color.pixel_fraction))
    #     colors['red'].append('red: {}'.format(color.color.red))
    #     colors['green'].append('green: {}'.format(color.color.green))
    #     colors['blue'].append('blue: {}'.format(color.color.blue))
    #     colors['opacity'].append('opacity: {}'.format(color.color.alpha))

    # return render_template('test.html', value=props)
