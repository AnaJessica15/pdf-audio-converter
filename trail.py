# path of the PDF file
import pyttsx3
import PyPDF2

path = open('/home/ana/ana/pdf-audio-converter/sample.pdf', 'rb')
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
  
# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(1)
  
# extracting the text from the PDF
text = from_page.extractText()
  
# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

# import pyttsx3
# import pdfplumber
# import PyPDF2

# file = 'C:/Users/<user_name>/Desktop/Book.pdf'

# #Creating a PDF File Object
# pdfFileObj = open(file, 'rb')

# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# #Get the number of pages
# pages = pdfReader.numPages

# with pdfplumber.open(file) as pdf:
#  #Loop through the number of pages
#     for i in range(0, pages): 
#       page = pdf.pages[i]
#       text = page.extract_text()
#       print(text)
#       speaker = pyttsx3.init()
#       speaker.say(text)
#       speaker.runAndWait()