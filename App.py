from flask import Flask, render_template, request
from models.user import User
import json

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, world!'

@app.route('/user/<id>', methods=['GET'])
def getUserById(id):
  if request.method == 'GET':
    user = User()
    response = user.showOneUserById(id)
    return json.dumps(response[0])

@app.route('/user/', methods=['POST'])
def getUserByUsername():
  if request.method == 'POST':
    user = User()
    username = request.form['username']
    response = user.showOneUserByUsername(username)
    return json.dumps(response[0])

@app.route('/new_user/', methods=['POST'])
def createUser():
  if request.method == 'POST':
    user = User()
    nombre = request.form['nombre']
    username = request.form['username']
    password = request.form['password']
    response = user.createUser(nombre, username, password)
    print(response)
    return response

if __name__ == '__main__':
  app.run(port = 8080, debug = True)
