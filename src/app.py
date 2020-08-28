import os
import sys

from flask import Flask, jsonify, request, render_template
from nlpCode.pdfToCsv import *
from nlpCode.frequentWords import *


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    dataFrame = pd.DataFrame()
    target = os.path.join(APP_ROOT, "temp/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)

        filename = file.filename
        destination = "/".join([target, filename])

        print(destination)

        file.save(destination)
        data = dataFrame.append({"data": pdfToCsv(destination, "")}, ignore_index=True)

        os.remove(destination)
        os.remove(destination + ".csv")

        text = data.data[0]

        toBeSend = frequentAndEssentialWords(text)

        print(toBeSend)

        return render_template("complete.html", toBeSend=toBeSend)


@app.route("/upload_text", methods=["POST"])
def upload_text():
    dataFrame = pd.DataFrame()
    target = os.path.join(APP_ROOT, "temp")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)

        filename = file.filename
        destination = "/".join([target, filename])

        file.save(destination)

        data = dataFrame.append({"data": textToCsv(destination)}, ignore_index=True)

        os.remove(destination)
        os.remove(destination + ".csv")

        text = data.data[0]

        toBeSend = frequentAndEssentialWords(text)

        print(toBeSend)

        return render_template("complete.html", toBeSend=toBeSend)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
