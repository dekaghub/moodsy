from flask import Flask, render_template
from requests import post


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")
    # fileobject = request.files["file2upload"]
    # filename = secure_filename(fileobject.filename)
    # save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    # fileobject.save(save_path)
    # return "successful_upload"

if __name__ == '__main__':
    app.run (debug=True)