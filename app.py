from flask import Flask, render_template, request, redirect, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import pyttsx3 
import PyPDF2
# import pymongo
# from pymongo import MongoClient


UPLOAD_PATH = "static/"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    global filename
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


    return '', 204

def create_audio():

    pdf_file = open('sample.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
 
    number_of_pages = read_pdf.getNumPages()

    engine = pyttsx3.init()

    for i in range(0, number_of_pages ):
 
        page = read_pdf.getPage(i)
        
        page_content = page.extractText()

        print(page_content)
    
        newrate=120
        engine.setProperty('rate', newrate)
        newvolume=3
        engine.setProperty('volume', newvolume)
            
        # engine.say(page_content) 

        engine.save_to_file(page_content,os.path.join(app.config['UPLOAD_FOLDER'], filename+'.mp3')) 
        
        engine.runAndWait()

    return filename


@app.route('/play', methods = ["GET","POST"])
def play():
 
    return render_template('play.html',filename = filename)




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")