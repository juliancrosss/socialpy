from flask_wtf import Form
from modelos import User
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email
                                Length, EqualTo)
  def name_exists(from, field):
    if User.select().where(User.username == field.data).exists():
      raise ValidationError('Usuario con este nombre ya existe.')
      
   def email_exists(from, field):
    if User.select().where(User.email == field.data).exists():
      raise ValidationError('Usuario con este email ya existe.')

   class RegistracionUsuarios(Form):
        usuario = StringField(
             'Usuario',
              validators=[
                DataRequired(),
                Regexp(
                   r'^[a-zA-Z0-9_]+$',
                      message=("Usuario debe contener letras, palabras, numeros o guiones bajos.")
                ),
                name_exists
              ])
          email = StringField(
              'Email',
              validators=[
                DataRequired(),
                Email(),
                email_exists
              ])
         password = PasswordField(
           'Password',
           validators=[
              DataRequired(),
              Length(min=2),
              EqualTo('password2', message= 'Contraseña debe coincidir ')
           ])
    password2 = PasswordField(
            'Confirmar Contraseña'
             validators=[
              DataRequired(),
            ])

