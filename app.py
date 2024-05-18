from flask import Flask, render_template
from datetime import datetime
from jogadores import jogadores
import jinja_partials
app = Flask(__name__)
jinja_partials.register_extensions(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jogadores')
def lista_jogadores():
   return render_template('jogadores.html', jogadores=jogadores)


@app.route('/hora_certa')
def hora_certa():
    import time
    time.sleep(5)
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time


if __name__ == '__main__':
  app.run(port=5000, debug=True)
 