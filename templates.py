from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CsrfProtect
from flask import session, redirect, url_for, flash
import forms
import loginForm


app = Flask(__name__, template_folder="template")
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

@app.route("/", methods = ['GET','POST'])
def home():
    if 'Usuario' in session:
        usuario = session['Usuario']
        print(usuario)
    formulario = forms.formulario(request.form)
    if  request.method == "POST" and formulario.validate():
        print (formulario.Palabra.data) 
        print (formulario.Significado.data) 
        print (formulario.Correo.data) 
    n ="Mauricio"
    return render_template("template.html", nombre = n, form = formulario)

@app.route("/login", methods = ['GET','POST'])
def login():
    logForm = loginForm.logForm(request.form)
    if  request.method == "POST" and logForm.validate(): 
        usuario = logForm.Usuario.data
        flash('Bienveido {}'.format(usuario))
        session['Usuario'] = logForm.Usuario.data
    return render_template("tem_log.html", form = logForm)

@app.route("/logout", methods = ['GET','POST'])
def logout():
    if 'Usuario' in session:
      session.pop('Usuario') 
    return redirect(url_for('login'))


if __name__ == '__main__':
 app.run(debug=True, port=8000)