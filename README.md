# PII-LexNLP
Helps detect Personal Identifiable Information from Image file

This project facilitates fetching the following personal Identifiable Information from images/ screenshots

 - SSN
 - Phone Number

Steps to set the project along with python packages. This is a flask web framework and it needs some python packages for the functionality to work.

1. Clone the proect
2. CD to the project directory
3. We need pip to install python packages. In case you do not have pip, use curl command to download get-pip.py and install by the command, 
   'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py' and then 'python get-pip.py'
4. Install pipenv for virtual environment to isolate the working environment from global setup by the command 'pip install pipenv'
5. Activate pipenv by the command 'pipenv shell'
6. Install Pillow library which is needed for Image processing by the command 'pipenv install pytesseract Pillow'
7. Now clone another project in the same directory by the command 'git clone https://github.com/LexPredict/lexpredict-lexnlp.git', then 'cd lexpredict-lexnlp' and 
   install the dependency by command 'pipenv install'
8. Here during the installation you may face some comppilation issues related to scipy and pandas. But ignore them. As soon as the dependencies are installed, 
   come out of the folder by command 'cd..'.
9. Here we need to install flask by the command 'pipenv install flask'. This is the web framework to start the server and render HTML files
10. All the necessary scripts and HTML files needed are present in the original code. so you do not need to worry regarding the HTML files and python scripts.
11. Make sure pipenv is activated. If not run the commad 'pipenv shell'
12. Now run 'flask run'
13. As soon as you run the above comamnd you can open the home page by loading 127.0.0.1:5000 (index.html)
14. Click the upload link and then upload any snapshot or image which has some kind of PII and click upload
15. You should see result displaying fetched textual information and PIIs
