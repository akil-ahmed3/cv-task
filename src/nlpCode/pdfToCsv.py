import json
import pdftotext
import pandas as pd

import os


def pdfToCsv(filename, dir):
    with open(dir + filename, "rb") as f:
        pdf = pdftotext.PDF(f)

    with open("./" + dir + "./output.txt", "w") as f:
        f.write("\n".join(pdf))

    df = pd.read_csv("./" + dir + "/output.txt", delimiter="/n")
    df.to_csv(filename + ".csv")
    dff = pd.read_csv(filename + ".csv")

    return ",".join(dff.Contact)


def textToCsv(filename):
    df = pd.read_csv(filename, delimiter="/n")

    df.to_csv(filename + ".csv")
    dff = pd.read_csv(filename + ".csv")

    return ",".join(dff.Contact)
