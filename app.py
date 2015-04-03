from flask import Flask, g
from flask.ext.login import LoginManager

import modelos

  DEBUG = True
  PORT = 8000
  HOST = '0.0.0.0'
  
  app = Flask(__name__)
  app.secret_key ='auesh.bouoasthu.43,jdkfhksafhskjfsdjjkadfdjdhfk'
  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = 'login'
  
  @login_manager.user_loader
    def load_user(userid):
      try:
        return modelos.User.get(models.User.id == userid)
           except models.DoesNotExist:
          return None
  
  @app.before_request
  def before_request():
    """Connect to the database before each request."""
    g.db = modelos.DATABASE
    g.db.connect()
    
   @app.after_request
   def before_request(response):
      """Close the database connectiong after each request."""
     g.db.close()
     return response
     
     
     
  if __name__ == '__main__':
    models.initialize()
    models.User.create_user(
       name = 'juliancruz'
       contraseña = 'contraseña',
       email ='freakcruz@me.com',
       administrador = True
       )
    app.run(debug=DEBUG, host=HOST, port=PORT)
