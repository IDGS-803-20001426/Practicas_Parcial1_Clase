from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, FloatField

class UsersForm(Form):
    color1=SelectField('color1', 
                       choices=[('negro', 'Negro'), 
                                ('cafe', 'Cáfe'), 
                                ('rojo', 'Rojo'), 
                                ('naranja', 'Naranja'), 
                                ('amarillo', 'Amarillo'), 
                                ('verde', 'Verde')
                                , ('azul', 'Azul')
                                , ('violeta', 'Violeta')
                                , ('gris', 'Gris')])
    color2=SelectField('color2', 
                       choices=[('negro', 'Negro'), 
                                ('cafe', 'Cáfe'), 
                                ('rojo', 'Rojo'), 
                                ('naranja', 'Naranja'), 
                                ('amarillo', 'Amarillo'), 
                                ('verde', 'Verde')
                                , ('azul', 'Azul')
                                , ('violeta', 'Violeta')
                                , ('gris', 'Gris')])
    color3=SelectField('color3', 
                       choices=[('negro', 'Negro'), 
                                ('cafe', 'Cáfe'), 
                                ('rojo', 'Rojo'), 
                                ('naranja', 'Naranja'), 
                                ('amarillo', 'Amarillo'), 
                                ('verde', 'Verde')
                                , ('azul', 'Azul')
                                , ('violeta', 'Violeta')
                                , ('gris', 'Gris')])
    tolerancia=RadioField('tolerancia',
                          choices=[('dorado', 'Dorado'),('plata', 'Plata')])