from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class formulario (Form):
    Palabra = StringField("palabra",
    [
        validators.Required(message='Es requerida una palabra'),
        validators.Length(min=3, max=16, message='Ingrese una palabra coherente')
    ])
    Significado = StringField("significado",
        [
        validators.Required(message='Es requerida una significado'),
        validators.Length(min=3, max=25, message='Ingrese una significado acorde a la palabra')
    ])
    Correo = EmailField("email")