from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class FormArchivoRegistro(Form):
    reg_ingles=StringField('Ingles',{
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3, message='Ingresa una palabra valida')
    })

    reg_espanol=StringField('Español',{
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3, message='Ingresa una palabra valida')
    })

class FormArchivoBusqueda(Form):
    select_idioma=RadioField('Idioma', 
                             choices=[('espanol', 'Español'), ('ingles', 'Ingles')],
                             render_kw={"class": "custom-radio-field"}                         
    )

    leer_reg=StringField('Palabra',{
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3, message='Ingresa una palabra valida')
    })

    resultado=StringField('Traducción', render_kw={'disabled': True})