try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import PyPDF2 

def ocr_extraction(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  
    return text

def pdf_extract(filename):
    print (filename)
    pdfFileObj = open(filename,'rb')  
    
    # creating a pdf reader object  
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
    
    # printing number of pages in pdf file  
    print(pdfReader.numPages)  
    
    # creating a page object  
    pageObj = pdfReader.getPage(0-1)  
    
    # extracting text from page  
    print('**'+pageObj.extractText())  
    
    # closing the pdf file object  
    pdfFileObj.close()  
    return pageObj.extractText()


#print(ocr_core('./OCR.png'))
