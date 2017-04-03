# -*- coding: UTF-8 -*-
from flask import Flask
from flask import jsonify
from flask import request

import os
import sqlite3
import json

from models.posts import Posts

##
# Configs da API
##
app = Flask(__name__)
app.config.from_object(__name__)

##
# Configs
##
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'api.db'),
    SECRET_KEY='secret',
    USERNAME='admin',
    PASSWORD='admin'))
    
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

##
# Retorna uma instancia do banco de dados SQLite
##
def get_db():
    if not hasattr(app, 'api'):
        app.sqlite_db = connect_db()
    return app.sqlite_db

##
# Cria o banco de dados se o mesmo não existir
##
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

##
# @Cli - Um comando em Shell que cria o banco de dados
##
@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Criando o banco de dados')

##
# Fecha a conexão com o banco de dados no final do request
##
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(app, 'sqlite_db'):
        app.sqlite_db.close()

##
# UTILS
##
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

##
# Lista todos os posts
# Ex curl -X GET http://localhost:5000/posts
##
@app.route('/posts')
def post_list():
    model = Posts(get_db())
    posts = model.selectall()

    response = jsonify(posts)
    response.status_code = 200
    return response 

##
# Retorna a postagem informada pelo ID
# Ex: curl -X GET http://localhost:5000/posts/1
##
@app.route('/posts/<int:id>')
def post_get(id):
    model = Posts(get_db())
    posts = model.selectmessage(id)

    response = jsonify(posts)
    response.status_code = 200
    return response 

##
# Cria um novo post
# Ex: curl -X POST http://localhost:5000/posts -H "Content-Type: Application/json" -d '{"user":"@fidelissauro", "message":"Bife de figado e muito ruim"}'
##
@app.route('/posts', methods=['POST'])
def post_create():
    postdata = request.get_json(silent=True)

    model = Posts(get_db())
    newpost = model.insert(user=postdata['user'], message=postdata['message'])

    response = jsonify(newpost)
    response.status_code = 201 #Created! 
    return response


##
# Atualiza um post
##
@app.route('/posts/<int:id>', methods=['PUT', 'PATCH'])
def post_update(id):
    response = jsonify({"status" : "atualizado"})
    response.status_code = 202
    return response

##
# Deleta um Posts
# Ex: curl -X DELETE http://localhost:5000/posts/3
##
@app.route('/posts/<int:id>', methods=['DELETE'])
def post_delete(id):
    model = Posts(get_db())
    model.delete(id)
    response = jsonify({"status" : "deletado"})
    response.status_code = 204
    return response


if __name__ == "__main__":
  app.run()
