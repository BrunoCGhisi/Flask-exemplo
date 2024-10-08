from flask import request
from database.db import db
from models.cargos import Cargos

def cargosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            cargo = Cargos(data['nome'])
            db.session.add(cargo)
            db.session.commit()
            return 'Cargo adicionado com sucesso!', 200
        except Exception as e:
            return 'Nao foi possivel inserir o cargo! ERRO:{}'.format(str(e)),400
    
    elif request.method == 'GET':
        try:
            data = Cargos.query.all()
            newData = {'cargos': [cargo.to_dict() for cargo in data]}
            
            return  newData, 200
        except Exception as e:
            return 'Nao foi possivel inserir o cargo! ERRO:{}'.format(str(e)),400