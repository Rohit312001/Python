# Convert PDF to Audio

### Pre-requisites:

- So First we install the required packages named as `pdfplumber`

```python
pip3 install pdfplumber
```

![Screenshot from 2023-11-11 13-08-52](https://github.com/Rohit312001/GitDemo/assets/76991475/7b5b0c99-36e2-4eac-9d95-d19066c41adf)

- So First we install the required packages named as `pyttsx3`

```python
pip3 install pyttsx3
```

![Screenshot from 2023-11-11 12-04-30](https://github.com/Rohit312001/GitDemo/assets/76991475/e52a7ec7-89e0-42aa-88ce-96fa2f32fabc)

- **(For Linux Users)** download `espeak` package because pyttsx3 uses espeak as a backend for linux.

```bash
sudo apt-get install espeak
```

![Screenshot from 2023-11-11 12-50-11](https://github.com/Rohit312001/GitDemo/assets/76991475/bff07aff-1207-42e1-825e-450b0fc2f9ac)

### Process:

- **This line is a Python import statement. It's used to include the "pdfplumber" module from the "pdfplumber" package in your Python code.**

```python
import pdfplumber
```

- **This line is a Python import statement. It's used to include the "pyttsx3" module from the "pyttsx3" package in your Python code.**

```python
import pyttsx3
```

- Now we will named a variable as "file" in which we will assign the path of the pdf file which we want to convert into audio file.

```python
# In your case, you will need to change the path to the PDF file you want to convert:
file = "./path/to/pdf/file.pdf"
```

- Now we will open the pdf file using with open() function and named it as "pdf".

```python
# By using the with statement, you ensure that the pdf file is closed properly when you exit the indented block.
with pdfpluber.open(file) as pdf:
```

- Now we will named a variable as "pages" in which we will assign the total number of pages in the pdf file.

```python
# This will get the total number of pages in the PDF document.
    pages = len(pdf.pages)
```

- Now we will named a variable as "speaker" in which we will assign the pyttsx3.init() function.

```python
# This will initialize the pyttsx3 module.
    speaker = pyttsx3.init()
```

- Here we will Adjust the rate of the speaker.

```python
# This will adjust the rate of the speaker.
rate= speaker.getProperty('rate')
speaker.setProperty('rate', 105)
```

- Here we will Adjust the volume of the speaker.

```python
# This will adjust the volume of the speaker.
volume = speaker.getProperty('volume')
speaker.setProperty('volume',1.0)
```

- Now we will create a loop in which we will iterate the pages of the pdf file.

```python
# This will iterate through the pages of the PDF document.
    for i in range(0,pages):
```

- Now we will named a variable as "page" in which we will assign the pdf.pages[i] function.

```python
# This will get the page number of the PDF document.
        page = pdf.pages[i]
```

- Now we will named a variable as "text" in which we will assign the page.extract_text() function.

```python
# This will extract the text from the PDF document.
        text = page.extract_text()
```

- Now we will print the text.

```python
# This will print the text from the PDF document.
        print(text)
```

- Here we will speak the text.

```python
# This will speak the text from the PDF document.
        speaker.say(text)
```

- Here we will run the speaker.

```python
# This will run the speaker.
    speaker.runAndWait()
```

### Summary:

- So,this code initializes a **PDF-to-Audio** conversion using the "pdfplumber" and "pyttsx3" package, specifying the input **PDF file**, the output **Audio file**, and then performs the conversion, and closes the process when finished.

---

### OUTPUT:

- Python Code Runned Successfully on Terminal.

![image](https://github.com/Rohit312001/GitDemo/assets/76991475/1c712cc0-8bcf-4003-a5e2-fc95e39e81f6)

---
