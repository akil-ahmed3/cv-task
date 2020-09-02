import os
import sys

from flask import Flask, jsonify, request, render_template
from nlpCode.pdfToCsv import *
from nlpCode.frequentWords import *
from nlpCode.fiftyPdf import *

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def format_data(tf, frequent):
    new_tf = json.loads(tf.to_json())
    new_frequent = json.loads(frequent.to_json())
    new_frequent_dict = {}

    for f in new_frequent["0"].keys():
        new_frequent_dict[new_frequent["0"][f]] = new_frequent["1"][f]

    to_be_send = {"tf_idf": new_tf["TF-IDF"], "frequent": new_frequent_dict}

    return to_be_send


@app.route("/")
def index():
    data = fifty_data_func("../profiles/")
    fify_pdf_array = []
    for item in data:
        (tf, frequent) = item

        single_data = format_data(tf, frequent)

        fify_pdf_array.append(single_data)

    return render_template("upload.html", data=fify_pdf_array)


@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    dataFrame = pd.DataFrame()
    target = os.path.join(APP_ROOT, "temp/")

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):

        filename = file.filename
        destination = "/".join([target, filename])

        file.save(destination)
        data = dataFrame.append({"data": pdfToCsv(destination, "")}, ignore_index=True)

        os.remove(destination)
        os.remove(destination + ".csv")

        text = data.data[0]

        (tf, frequent) = frequentAndEssentialWords(text)

        to_be_send = format_data(tf, frequent)

        return render_template("complete.html", toBeSend=to_be_send)


@app.route("/upload_text", methods=["POST"])
def upload_text():
    dataFrame = pd.DataFrame()
    target = os.path.join(APP_ROOT, "temp")

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):

        filename = file.filename
        destination = "/".join([target, filename])

        file.save(destination)

        data = dataFrame.append({"data": textToCsv(destination)}, ignore_index=True)

        os.remove(destination)
        os.remove(destination + ".csv")

        text = data.data[0]

        (tf, frequent) = frequentAndEssentialWords(text)

        to_be_send = format_data(tf, frequent)

        return render_template("complete.html", toBeSend=to_be_send)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
