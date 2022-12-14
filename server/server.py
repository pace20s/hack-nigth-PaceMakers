import os  # For File Manipulations like get paths, rename
from flask import Flask, request, render_template
import openai
# import wget
# import pathlib
import pdfplumber
import numpy as np
from twilio.rest import Client
# PaperFilePath = "./sample2.pdf"

account_sid = "AC4fe03fe7e0b561f68567b0208c6e4d68"
auth_token = "55b1799faa0a1c9aa2911e18d5b5a701"
client = Client(account_sid, auth_token)


def sendMessage(message, mobNumber):
    message = client.messages.create(body=message,
                                     from_="+18316043309",
                                     to="+91" + mobNumber)

    print("message send" + str(message.sid))


def showPaperSummary(paperContent, mobNum):
    tldr_tag = "\n tl;dr:"
    openai.organization = 'org-CCY2sGmfLZVuGLoQQ3I1ScxI'
    openai.api_key = "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"
    engine_list = openai.Engine.list()

    for page in paperContent:
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(engine="davinci",
                                            prompt=text,
                                            temperature=0.3,
                                            max_tokens=140,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            stop=["\n"])
        messageText = (response["choices"][0]["text"]).replace("I", "You")
        sendMessage(messageText, mobNum)
        print(messageText)


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
        # get data from the frontend
        f = request.files["file"]
        mobNumber = str(request.form["mobNumber"])
        print("Send text to: " + mobNumber)

        #save file to local storage
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        PaperFilePath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        print(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))

        #call the gpt3 api and send text message
        paperContent = pdfplumber.open(PaperFilePath).pages
        showPaperSummary(paperContent, mobNumber)

        return "file saved"
