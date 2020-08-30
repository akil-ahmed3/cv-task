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

        (tf, frequent) = frequentAndEssentialWords(text)

        print(tf.to_json())
        print(frequent.to_json())

        new_tf = json.loads(tf.to_json())
        new_frequent = json.loads(frequent.to_json())
        new_frequent_dict = {}

        for f in new_frequent["0"].keys():
            new_frequent_dict[new_frequent["0"][f]] = new_frequent["1"][f]

        to_be_send = {"tf_idf": new_tf["TF-IDF"], "frequent": new_frequent_dict}

        print(to_be_send)

        return render_template("complete.html", toBeSend=to_be_send)


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

        (tf, frequent) = frequentAndEssentialWords(text)

        new_tf = tf.to_json(tf)
        new_frequent = frequent.to_json(frequent)

        to_be_send = {"tf": new_tf, "frequent": new_frequent}

        print(to_be_send)

        return render_template("complete.html", toBeSend=to_be_send)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
