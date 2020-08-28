## Description:

**Task 1**
50 downloaded profiles are inside **profiles** folder in root folder

**Task 2**
To run Task two:

1. Open your terminal
2. type "python python src/nlpCode/fiftyPdf.py"

process:

1. Here I used pdftotext libray to convenrt my pdf to text.
2. Then converted that text csv file
3. The called the function to get the most frequent and essential words, which I wll explain in step 3
4. printing those values in **terminal** as **csv** format

**Task 3**
If you go inside **src/nlpCode/** directory there you will find **frequentWords.py** file, this is a function which I am calling wherever I need.

Process:

1. I have used sklearn libray to extract frequent and essenytial words
2. created a function, fron there returned them in csv format.

**Task 4**
For fourth task I have used flask and jinja2

Process:

1. there are two routes
   - *http://127.0.0.1:5000/upload_text* nd
   - *http://127.0.0.1:5000/upload_pdf*
2. Open terminal and type
   - cd src
   - flask run
3. Open this link in the browser *http://127.0.0.1:5000*
4. There are two fields one is to upload pdf and other is for text
5. The result you can see in you terminal, browser console or webpage(this one is ugly)
