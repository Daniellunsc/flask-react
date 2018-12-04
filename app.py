from flask import Flask, render_template, jsonify


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

# template_folder = Pasta de templates para renderizar o index.html
# static_folder = Pasta de arquivos estáticos
app = Flask(__name__, template_folder='client/build', static_folder='client/build/static')

# Qualquer rota fora as configuradas servem a aplicação REACT.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def any_route(path):
  return render_template('index.html')

@app.route('/rest')
def rest():
  return jsonify(message="Oi")

@app.route('/name', defaults={'username': ''})
@app.route('/name/<username>')
def name(username):
  return jsonify(name=username)

if __name__ == "__main__":
  app.run(debug=True)