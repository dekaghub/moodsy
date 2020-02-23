from flask import Flask, render_template, request, redirect, jsonify
from requests import post
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename)
        save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], fname)
        f.save(save_path)

        with open(save_path, "r") as f:
            pass

        return 'file uploaded successfully'

# @app.route('/sendfile', methods=['POST', 'GET'])
# def sendfile():
#     fileobject = request.files["file2upload"]
#     filename = secure_filename(fileobject.filename)
#     save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
#     fileobject.save(save_path)
#     return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
