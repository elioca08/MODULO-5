from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms import validators

class logForm (Form):
    Usuario = StringField("usuario",
    [
        validators.Required(message='Es requerido el nombre de usuario'),
        validators.Length(min=8, max=16, message='Ingrese un nombre de usuario coherente')
    ])
    Password = PasswordField("constraseña",
    [
        validators.Required(message='Es requerido la contraseña'),
        validators.Length(min=8, max=16, message='Ingrese la contraseña correspondiente')
    ])