# -*- coding: UTF-8 -*-
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/ola')
def hello_world():
    message = {"message":"olá!"}
    response = jsonify(message)
    response.status_code = 200
    return response 

@app.route('/hateoas')
def hateoas():
    message = {"pedido": {
            "id" : 123, 
            "produto" : "dorflex"
        },
        "links" : [
                {"GET": "/pedido/123"},
                {"PUT": "/pedido/123"},
                {"DELETE": "/pedido/123"}
                ]
        }
    response = jsonify(message)
    response.status_code = 200
    return response 


if __name__ == "__main__":
  app.run()
