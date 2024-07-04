from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
  return '<p>Sophia: wtf</p><br><p>Kevin: idk</p><br><p>Nancy: jk</p><br>'
  
@app.route('/daniela')
def t_test():
   return render_template('index1.html')

@app.route('/myimage')
def hello2():
  return render_template('imag.html')

#este ultimo me muestra una imagen