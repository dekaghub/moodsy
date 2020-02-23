from flask import Flask, render_template, request, redirect, jsonify
from requests import post
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER']= 'uploads'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/sendfile', methods=['POST', 'GET'])
def sendfile():
    fileobject = request.files["file2upload"]
    filename = secure_filename(fileobject.filename)
    save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    fileobject.save(save_path)
    return "successful_upload"


if __name__ == '__main__':
    app.run (debug=True)