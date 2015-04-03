import datetime
from flask.ext.bcrypt import generate_password_hash
from flask.ext-login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('social.db')

class Usuario(UserMixin, Model):
    usuario = CharField(unique=True)
    contraseña = CharField(max_length=100)
    email = CharField(unique=True)
    fecha_de_registro = DateTimeField(default=datetime.datetime.now)
    es_administrador = BooleanField(default=False)
  
class Meta:
     database = DATABASE
     ordenado_por = ('-fecha_de_registro',)
@classmethod    
def crear_usuario(cls, usuario, contraseña, email, administrador=False):
     try:
        cls.create(
             usuario=usuario,
             contraseña=generate_password_hash(contraseña),
             email=email,
             es_administrador=administrador)
     except IntegrityError:
         raise ValueError("Usuario ya existe")
     
