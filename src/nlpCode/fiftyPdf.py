from nlpCode.pdfToCsv import *
from nlpCode.frequentWords import *

import json
import pdftotext
import pandas as pd

import os


def fifty_data_func(dir):

    data = pd.DataFrame()

    fifty_data = []

    for filename in os.listdir(dir):
        if filename.endswith(".pdf"):
            data = data.append({"data": pdfToCsv(filename, dir)}, ignore_index=True)
            os.remove(filename + ".csv")
            # os.remove("../output.txt")
            continue
        else:
            continue

    data.to_csv("fifty.csv")

    df = pd.read_csv("./fifty.csv")

    texts = df.data

    for text in texts:
        toBePrinted = frequentAndEssentialWords(text)
        fifty_data.append(toBePrinted)

    return fifty_data