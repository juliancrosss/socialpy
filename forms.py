from flask_wtf import Form

from models import User


class RegisterForm(Form):
      username= StringField(
          'Username',
          validators=[
                DataRequired(),
                Regexp(
                     r'^[a-zA-Z0-9_]+$',
                     message="Username should be one word, letters, numbers, and underscores only")
                     
                     
