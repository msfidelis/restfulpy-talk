from flask import Flask
from flask import jsonify
from flask import request

import os
import sqlite3

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'api.db'),
    SECRET_KEY='secret',
    USERNAME='admin',
    PASSWORD='admin'))
    
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/posts')
def post_list():
    posts = ['legal', 'fodase']
    response = jsonify(posts)
    response.status_code = 200
    return response 

@app.route('/posts', methods=['POST'])
def post_create():
    response = jsonify({"status" : "criado"})
    response.status_code = 201
    return response

@app.route('/posts', methods=['PUT', 'PATCH'])
def post_update():
    response = jsonify({"status" : "atualizado"})
    response.status_code = 202
    return response

@app.route('/posts', methods=['DELETE'])
def post_delete():
    response = jsonify({"status" : "deletado"})
    response.status_code = 204
    return response


if __name__ == "__main__":
  app.run()
