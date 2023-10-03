'''Write a programn to manipulate pdf files using pyPDF. Your programs should be able to merge multiple 
pdf files into a single pdf. You're welcome to add more functionalities'''

'''pyPDF is a free and open-source pure-python PDF library capable of splitting, merging, cropping and 
transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to pdf
files. pypdf can retrieve text and metadata from PDFs as well'''

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
print(type(merger))
files = [file for file in os.listdir() if file.endswith('.pdf')]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()