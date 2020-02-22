import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service-account-token.json'

client = vision.ImageAnnotatorClient()

# image file
image_location = 'image.jpg'

with io.open(image_location, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content = content)

response = client.face_detection(image = image)
faces = response.face_annotations

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

for face in faces:
    print('face #')
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    print('sorrow: {}'.format(likelihood_name[face.sorrow_likelihood]))
    print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))