from flask import Flask, request, redirect, jsonify, render_template
import os, io
from werkzeug.utils import secure_filename
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from google.cloud import vision

#google creds
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service-account-token.json'

#spotify creds
clientID = '5e3b1a5db9854632bf9207c20eb44424'
clientSecret = '0c093a2a8bb24aa8bee9b5ff36866cc5'

client_creds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_creds)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'



@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/sendfile", methods=["POST"])
def send_file():
    fileob = request.files["file2upload"]
    filename = secure_filename(fileob.filename)
    save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    fileob.save(save_path)
    return "successful_upload"

def process_image():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
