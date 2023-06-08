from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

from flask import render_template

@app.route('/films/list')
def list_films(name=None):
    return render_template('film_list.html', name=name)



# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)