# This line is a Python import statement. It's used to include the "converter" module from the "pdf2docx" package in your Python code.

from pdf2docx import Converter

pdf_file = "./Convert PDF to Docx/Grafana-1.pdf"

docx_file = "./Convert PDF to Docx/Grafana-1.docx"

cv = Converter(pdf_file)

cv.convert(docx_file)

cv.close()
