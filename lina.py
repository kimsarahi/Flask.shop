import sqlite3
from flask import Flask,redirect,render_template

from flask import request

from werkzeug.utils import secure_filename

import os



app = Flask(name)
UPLOAD_FOLDER = 'static/uploads'

# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER,exist_ok=True)


@app.route('/')
def homepage():
 return 'Hello'

@app.route('/add_product',methods=['GET','POST'])
def add_pr():
  if request.method=='POST':
    name = request.form.get('product','').strip()
    price = request.form.get('price','').strip()
    desc = request.form.get('decription','').strip()
    foto = request.files.get('image')
    filename = secure_filename(foto.filename)
    image_path = os.path.join(
    app.config['UPLOAD_FOLDER'],filename
    )
    foto.save()
    print(name,price,desc,image_path)
  return render_template('home.html')



#bug = error
if name=='main':
   app.run(debug=True)
# conn = sqlite3.connect('products.db')
# conn.execute('''
# CREATE TABLE IF NOT EXISTS products(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# product_name TEXT NOT NULL,
# price INTEGER NOT NULL,
# description TEXT NOT NULL,
# image TEXT NOT NULL
# )
# ''')
#int

# while start<=stop:
#     start = start  + 1