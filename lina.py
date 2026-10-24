import sqlite3
from flask import Flask,redirect,render_template

from flask import request

from werkzeug.utils import secure_filename

import os



app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER,exist_ok=True)



def connect_db():
  conn = sqlite3.connect('products.db0')
  conn.row_factory= sqlite3.Row
  return conn


@app.route('/')
def homepage():
  conn = connect_db()
  product = conn.execute ( 'SELECT * FROM products').fetchall()
  conn.close()
  return render_template('index.html',products=product)




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

    conn  = connect_db()

    conn.execute('''
INSERT INTO products ( product_name,price ,description,image)
VALUES(?,?,?,?)
''')(name,price,desc,filename)
    conn.commit()
    conn.close()
  # return render_template('.html')
  return render_template(add_products.html) 


#bug = error
if __name__=='__main__':
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