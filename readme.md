## Description:

**Task 1:**

50 downloaded profiles are inside **profiles** folder in root folder

**Task 2:**

To see task two:

1. Open your terminal
2. Type
   - `cd src`
   - `flask run`
3. Open this url (http://127.0.0.1:5000)
4. Here you can see Two things
   - From for uploading new files, and
   - 50 pdfs, divided into two tables "MOST ESSENTIAL WORDS" and "MOST FREQUENT WORDS".

PROCESS:

1. Here I used pdftotext libray to convenrt my pdf to text. One can find the code inside **pdfToCsv** function, inside **src/nlpCode/pdfToCsv.py**
2. Then converted that text csv file, One can find the code inside **textToCsv** function, inside **src/nlpCode/pdfToCsv.py**
3. Then called the function to get the most frequent and essential words, which I wll explain in step 3

**Task 3:**

If you go inside **src/nlpCode/** directory there you will find **frequentWords.py** file, this is a function which I am calling wherever I need to get most frequent and essential words.
Process:

1. I have used sklearn libray to extract frequent and essential words.
2. created a function, fron there returned them in csv formats in a tuple.

**Task 4:**

For fourth task I have used **flask, jinja2, html** and **css**

Process:

1. there are two routes
   - *http://127.0.0.1:5000/upload_text* **(POST REQUEST)**
   - *http://127.0.0.1:5000/upload_pdf* **(POST REQUEST)**
2. Open terminal and type, if you have done previously then leave it.
   - cd src
   - flask run
3. Open this link in the browser *http://127.0.0.1:5000*
4. There are two fields one is to upload pdf and other is for text
5. The result you can see in you in you next webpage, divided into two tables "MOST ESSENTIAL WORDS" and "MOST FREQUENT WORDS", 10 for each.
6. The codes resides in app.py in the root folder, there are two functions one is **upload_pdf** and **upload_text**, another function **format_data** is there to format the data.
