from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/xuxu",methods =  ['GET' ])
def get():
    data = {"mensagem":" lista de usuarios"}
    response = jsonify(data)
    response.status_code = 200
    return response

@app.route('/xuxu', methods = ['POST'])
def post():
    data = {"mensagem":"criado um usuario"}
    response = jsonify(data)
    response.status_code = 201
    return response

@app.route('/xuxu', methods = ['DELETE'])
def delete():
    data = {"mensagem":"deletado um usuario"}
    response = jsonify(data)
    response.status_code = 204
    return response
    
##
# Matheus e lindo
##
@app.route('/xuxu', methods = ['PUT'])
def put():
    data = {"mensagem":"atualizado um usuario"}
    response = jsonify(data)
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run()