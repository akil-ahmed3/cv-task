from pdfToCsv import *
from frequentWords import *

import json
import pdftotext
import pandas as pd

# nltk.download("punkt")
import os

data = pd.DataFrame()

for filename in os.listdir("./profiles"):
    if filename.endswith(".pdf"):
        data = data.append(
            {"data": pdfToCsv(filename, "./profiles/")}, ignore_index=True
        )
        os.remove(filename + ".csv")
        # os.remove("./output.txt")
        continue
    else:
        continue

data.to_csv("fifty.csv")

df = pd.read_csv("./fifty.csv")

texts = df.data

for text in texts:
    toBePrinted = frequentAndEssentialWords(text)
    print(toBePrinted)