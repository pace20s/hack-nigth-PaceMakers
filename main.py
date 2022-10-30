import PyPDF2 

def saveTxtFile(txt):
    f = open('sample.txt','w+')
    f.write(txt)
    f.close()

def pdfToText(file):
    # creating a pdf file object 
    pdfFileObj = open(file, 'rb') 
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    # creating a page object 
    pageObj = pdfReader.getPage(0) 
    # extracting text from page and pass to create txt func
    saveTxtFile(pageObj.extractText()) 
    # closing the pdf file object 
    pdfFileObj.close() 



pdfToText('./sample.pdf')