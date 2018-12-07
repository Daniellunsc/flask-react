from flask import Flask, render_template, jsonify, request, json
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models.user import User
from routes.Auth import Auth

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt, set_access_cookies, set_refresh_cookies)

"""

Como funcionar:
- Crie uma aplicação react usando o Create-React-App com o nome de client e coloque na pasta raiz do app.py

Ficará dessa maneira:

client/
  - src
  - ...
env/
app.py

"""
import routes.Auth

# template_folder = Pasta de templates para renderizar o index.html
# static_folder = Pasta de arquivos estáticos
app = Flask(__name__, template_folder='client/build', static_folder='client/build/static')


app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

CORS(app)

jwt = JWTManager(app)
app.register_blueprint(Auth)


# Qualquer rota fora as configuradas servem a aplicação REACT.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def any_route(path):
  return render_template('index.html')


@app.route('/rest')
@jwt_required
def rest():
  username = get_jwt_identity()
  resp = jsonify(message="Oi")
  
  return jsonify(message="Oi")

if __name__ == "__main__":
  app.run(debug=True)