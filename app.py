from flask import Flask, render_template, request, redirect, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import pyttsx3 
import PyPDF2
# import pymongo
# from pymongo import MongoClient


UPLOAD_PATH = "pdf/"
UPLOADED_PATH = "audio/"

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
app.config['UPLOADED_FOLDER'] = UPLOADED_PATH

@app.route('/', methods = ['GET', 'POST'])
def create_audio():
    
    if request.method == 'POST':
        
        uploaded_file    = request.files['file']

        global filename
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        global LOCAL_FILE_PATH
        LOCAL_FILE_PATH = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        pdf_file = open(UPLOAD_PATH+filename, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
    
        number_of_pages = read_pdf.getNumPages()

        # To access voice property of the speaker:
        # voices = speaker.getProperty('voices')
        # # Set the speaker's gender: 0-> Male (default), 1-> Female
        # speaker.setProperty('voice', voices[1].id)

        # engine = pyttsx3.init()
        engine = pyttsx3.init("espeak")

        for i in range(0, number_of_pages ):
    
            page = read_pdf.getPage(i)
            
            page_content = page.extractText()
            print(page_content)
        
            newrate=120
            engine.setProperty('rate', newrate)
            newvolume=3
            engine.setProperty('volume', newvolume)

            voices = engine.getProperty('voices')
            # for v in voices:
            #     print(v)

            engine.setProperty('voice',voices[11].id)

        # Set the speaker's gender: 0-> Male (default), 1-> Female
            # engine.setProperty('voice', voices[1].id)

            # engine.say(page_content) 
        file_ext = os.path.splitext(filename)[0]

        audio = os.path.join(app.config['UPLOADED_FOLDER'],file_ext+'.mp3') 

        engine.save_to_file(page_content,audio) 
        
        engine.runAndWait()

        return file_ext

    return render_template('upload.html')

# @app.route('/')
# def index():
#     return render_template('upload.html')

# @app.route('/', methods=['POST'])
# def upload_files():
#     uploaded_file = request.files['file']
#     global filename
#     filename = secure_filename(uploaded_file.filename)
#     if filename != '':

#         uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return filename


#     return '', 204

# @app.route('/submit', methods = ["POST"])
# def create_audio():
#     filename = upload_files()

#     pdf_file = open(UPLOAD_PATH+filename, 'rb')
#     read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
 
#     number_of_pages = read_pdf.getNumPages()

#     engine = pyttsx3.init()

#     for i in range(0, number_of_pages ):
 
#         page = read_pdf.getPage(i)
        
#         page_content = page.extractText()

#         print(page_content)
    
#         newrate=120
#         engine.setProperty('rate', newrate)
#         newvolume=3
#         engine.setProperty('volume', newvolume)
            
#         # engine.say(page_content) 
#         file_ext = os.path.splitext(filename)[0]
#         audio = os.path.join(app.config['UPLOAD_FOLDER'], filename+'.mp3')

#         engine.save_to_file(page_content,audio) 
        
#         engine.runAndWait()

#         print(audio)

#     return audio

@app.route("/view", methods=["GET","POST"])
def view():
    path = '/home/ana/ana/pdf-audio-converter/audio'

    files = os.listdir(path)
    data =[]
    
    for f in files:
        data.append(f)

    return render_template('view.html', result = data)

@app.route('/single', methods=["GET","POST"])
def display():

    audio_file = str(request.args['com_nam'])
 

    return render_template('play.html', filename = audio_file)





if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")