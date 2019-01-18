# coding: utf-8

import PyPDF2
from os import listdir

file = open("recibos.txt",'w')

for i in listdir():
    if str(i).find('.pdf')>1:
        pdfFileObj = open(i, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        texto = pageObj.extractText()
        #texto = str(texto).replace("\n","")
        file.write(str(texto))
