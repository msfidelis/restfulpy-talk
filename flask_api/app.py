# -*- coding: UTF-8 -*-
from flask import Flask
from flask import jsonify
from flask import request

import os
import sqlite3

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
    if not hasattr(app, 'sqlite_db'):
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
        apr.sqlite_db.close()

##
# UTILS
##
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


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
