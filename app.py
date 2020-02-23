from flask import Flask, request, redirect, jsonify, render_template, session
import os
import io
from werkzeug.utils import secure_filename
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from google.cloud import vision
import analyze_image


# google creds
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service-account-token.json'

# spotify creds
clientID = '5e3b1a5db9854632bf9207c20eb44424'
clientSecret = '0c093a2a8bb24aa8bee9b5ff36866cc5'


client_creds = SpotifyClientCredentials(
    client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_creds)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = "iLovmygorlfrein_wowSheCOOL"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/sendfile", methods=["POST"])
def send_file():
    fileob = request.files["file2upload"]
    filename = secure_filename(fileob.filename)
    save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    fileob.save(save_path)
    session["filepath"] = save_path
    return "successful_upload"


@app.route("/process", methods=["GET", "POST"])
def process_image():
    return analyze_image.facesearch(session["filepath"])


if __name__ == '__main__':
    app.run(debug=True)
