import os
from flask import Flask, render_template, request
from ocr_extraction import ocr_extraction,pdf_extract
from lexnlp_extraction import extract_pii


# define folder to save the uploaded image
UPLOAD_FOLDER = 'static/uploads/'

# Allowed file image file extension type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# validates file extension 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')

# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files.get('file')
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file.save(os.path.join(UPLOAD_FOLDER,file.filename))
            # OCR function extracts text
            extracted_text = ocr_extraction(file)
            # LexNLP extracts list of PIIs of possible different category
            pii = ", ".join(map(str, extract_pii(extracted_text)))
            # Sends the OCR extracted and LexMLP extracted texts
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,pii_text=pii,
                                   img_src=UPLOAD_FOLDER + file.filename)
        else:
            return render_template('upload.html', msg='Please enter correct file form')
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()
