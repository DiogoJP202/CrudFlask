from Usuario import Usuario
from flask import Flask, jsonify, request, render_template # type: ignore

_usuarios = []
app = Flask(__name__)

# CRUD

@app.route('/users', methods=['POST'])
def CreateUser():
    requisicao = request.get_json()
    print(requisicao)

    if not requisicao or 'nome' not in requisicao or 'email' not in requisicao:
        return jsonify({"Error": "requisição inválida!"}), 400
    
    usuario = Usuario(requisicao['nome'], requisicao['email'])
    _usuarios.append(usuario)
    
    return jsonify({"Message": "Usuário cadastrado!"}), 201

@app.route('/users', methods=['GET'])
def ListarUsuarios():
    return jsonify([u.to_dict() for u in _usuarios]), 200

@app.route('/users/<int:idUsuario>', methods=['GET'])
def GetUser(idUsuario):
    if not idUsuario:
        return jsonify({"Error": "ID de usuário inválido."}, 400)

    usuario = next((u for u in _usuarios if u._id == idUsuario), None)
    if usuario:
        return jsonify(usuario.to_dict()), 200
    return jsonify({"Erro": "Usuário não encontrado"}), 404


@app.route('/users', methods=['PUT'])
def UpdateUser():
    requisicao = request.get_json()
    print(requisicao)

    if not requisicao or 'nome' not in requisicao or 'email' not in requisicao or 'id' not in requisicao:
        return jsonify({"Error": "requisição inválida!"}), 400
    
    novoUsuario = Usuario(nome=requisicao['nome'], email=requisicao['email'])
    _usuarios.append(novoUsuario)
    
    return jsonify({"Message": "Usuário atualizado!"}), 201

@app.route('/users/<int:idUsuario>', methods=['DELETE'])
def DeleteUser(idUsuario):
    if not idUsuario:
        return jsonify({"Error": "ID de usuário inválido."}, 400)

    usuario = next((u for u in _usuarios if u._id == idUsuario), None)
    if usuario:
        _usuarios.remove(usuario)
        return jsonify({"Message": f"Usuário '{usuario.nome} - {usuario.email}' removido com sucesso!"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

# ROTAS:
@app.route('/')
def PaginaHome():
    nome = "Tonny"
    return render_template('index.html', nome=nome)

@app.route('/criarUsuarios', methods=['GET'])
def PaginaCriar():
    return render_template('criarUsuario.html')

@app.route('/verUsuarios', methods=['GET'])
def PaginaVer():
    return render_template('verUsuarios.html')

@app.route('/procurarUsuario', methods=['GET'])
def PaginaProcurar():
    return render_template('procurarUsuario.html')

@app.route('/atualizarUsuario', methods=['GET'])
def PaginaAtualizar():
    return render_template('atualizarUsuario.html')

@app.route('/excluirUsuario', methods=['GET'])
def PaginaExcluir():
    return render_template('excluirUsuario.html')

if __name__ == '__main__':
    app.run(debug=True)