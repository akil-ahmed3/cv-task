import json
import pdftotext
import pandas as pd
import re

import os


def pdfToCsv(filename, dir):
    with open(dir + filename, "rb") as f:
        pdf = pdftotext.PDF(f)

    with open("./" + dir + "./output.txt", "w") as f:
        f.write("\n".join(pdf))

    df = pd.read_csv("./" + dir + "/output.txt", delimiter="/n")
    df.to_csv(filename + ".csv")
    dff = pd.read_csv(filename + ".csv")

    text = ",".join(dff.Contact)
    new_text = re.sub(r"[^a-zA-Z]+", " ", text).lower()

    return new_text


def textToCsv(filename):
    df = pd.read_csv(filename, delimiter="/n")

    df.to_csv(filename + ".csv")
    dff = pd.read_csv(filename + ".csv")

    text = ",".join(dff.Contact)
    new_text = re.sub(r"[^a-zA-Z]+", " ", text).lower()

    return new_text
