from flask import request, render_template
from database.db import db
from models.clientes import Clientes


def clientesHtmlController():
    if request.method == 'GET':
        return render_template('clientesHTML.html')

def clienteController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user = Clientes(data['nome'], data['senha'], data['cargos_id'])
            print(data)
            db.session.add(user)
            db.session.commit()
            return 'Cliente criado com sucesso', 200
        except Exception as e:
            return 'O Cliente não foi criado com sucesso. Erro: {}'.format(str(e)), 405
        
    elif request.method == 'GET':
        try:
            data = Clientes.query.all();
            print([cliente.to_dict() for cliente in data])
            return render_template('clientes.html', data={'clientes': [cliente.to_dict() for cliente in data]})
        except Exception as e:
            return 'Não foi possível buscar Cliente. Erro: {}'.format(str(e)), 405
        
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            put_cliente_id = data['id']
            cliente = Clientes.query.get(put_cliente_id)
            if cliente is None:
                return {'error': 'Cliente nao encontrado'}, 404
            cliente.nome = data.get('nome', cliente.nome)
            cliente.senha = data.get('senha', cliente.senha)
            cliente.cargos_id = data.get('cargos_id', cliente.cargos_id)
            print(cliente.nome, cliente.senha, cliente.cargos_id)

            db.session.commit()
            return ('Cliente atualizado com sucesso')
        except Exception as e:
            return 'Nao foi possivel aturalizar o usuario. ERRO:{}'.format(str(e)),405

    elif request.method == 'DELETE':
        try:
            data = request.get_json()
            delete_cliente_id = data['id']
            cliente = Clientes.query.get(delete_cliente_id)

            if cliente is None:
                return {'error': 'Cliente nao foi encontrado'}, 404
            db.session.delete(cliente)
            db.session.commit()
            return 'Cliente deletado com sucesso', 200
        
        except Exception as e:
            return 'Nao foi possivel deletar o usuario. ERRO:{}'.format(str(e)), 405