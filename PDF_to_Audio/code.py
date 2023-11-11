# This line is a Python import statement. The "PyPDF2" and "pyttsx3" library is a Python module that allows you to generate Audio using python.
import pdfplumber
import pyttsx3

file = '/home/rohit/Documents/Python/PDF_to_Audio/How to Setup AWS Organization on Control Tower.pdf'

# Open the PDF file using pdfplumber
with pdfplumber.open(file) as pdf:
    # Get the total number of pages
    pages = len(pdf.pages)

    # Initialize the text-to-speech engine outside the loop
    speaker = pyttsx3.init()

    # Adjust speaking rate and volume
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', 105)  # Adjust the rate as needed

    volume = speaker.getProperty('volume')
    speaker.setProperty('volume', 1)  # Adjust the volume as needed

    # Loop through the number of pages
    for i in range(pages):
        page = pdf.pages[i]  # Access the specific page
        text = page.extract_text()
        print(text)
        # Speak the text for each page
        speaker.say(text)
        speaker.runAndWait()

# Stop the text-to-speech engine after processing all pages
speaker.stop()
