import os  # For File Manipulations like get paths, rename
from flask import Flask, request, render_template

app = Flask(__name__, static_folder="./static")

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
# if there exists no folder named uploads
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(path + "/uploads")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# index route
@app.route("/")
def index():
    return render_template("index.html")


# file upload route
@app.route('/upload', methods=["GET", "POST"])
def upload():
    # get the files property from request method and save the file in the uploads folder
    if request.method == 'POST':
        f = request.files["file"]
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return "file saved"
