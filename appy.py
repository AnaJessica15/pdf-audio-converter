# Import the python text to speech libarary and the PDF REader library
import pyttsx3 
import PyPDF2
# Read the PDF file binary mode
pdf_file = open('sample.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
#Find the number of pages in the PDF document
number_of_pages = read_pdf.getNumPages()
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init()
for i in range(0, number_of_pages ):
    # Read the PDF page 
    page = read_pdf.getPage(i)
    
    # Extract the text of the PDF page 
    page_content = page.extractText()
    
    # set the audio speed and volume
    newrate=120
    engine.setProperty('rate', newrate)
    newvolume=3
    engine.setProperty('volume', newvolume)
        
    # say method on the engine that passing input text to be spoken 
    engine.say(page_content) 

    engine.save_to_file(page_content,'sample.mp3') 
    
    # run and wait method to processes the voice commands.  
    engine.runAndWait()