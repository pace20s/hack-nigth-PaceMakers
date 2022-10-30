import os

path = os.getcwd()

UPLOAD_DIR = os.path.isdir(path + '/uploads')

if not UPLOAD_DIR:
    os.mkdir(path + "/uploads")
