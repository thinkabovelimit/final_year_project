from flask import Flask, render_template, request,flash,session
from flask_session import Session
import cv2
import numpy as np
import os
from werkzeug import secure_filename
app = Flask(__name__,template_folder='../templates',static_folder='../static')

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    print(key)
    return session.get('key', 'not set')

sess = Session()
sess.init_app(app)

upload_folder=os.path.abspath('../uploads')
app.config['upload_folder']=upload_folder
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}
template=os.path.abspath('../templates')
static=os.path.abspath('../static')
@app.route('/')
def display():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      if f.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
          return "Invalid file format"
      f.save(os.path.join(app.config['upload_folder'], f.filename))
      return 'file uploaded successfully'
def preprocess():
    image=cv2.imread('../uploads/f.filename')
    f=cv2.fastNlMeansDenoisingColored(image,None,6,6,7,21)
    width = int(200)
    height = int(200)
    dim = (width, height)
# resize image
    dst1 = cv2.resize(dst, dim, interpolation = cv2.INTER_AREA)

    dst1.save(os.path.join(app.config['upload_folder'], f.filename))


if __name__ == '__main__':
   app.run(debug = True)