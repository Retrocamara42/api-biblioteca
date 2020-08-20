from flask import  request, jsonify
from flask_restful import Resource
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:////biblioteca.db')

class list_authors(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT id,apellido FROM author ORDER BY apellido DESC")
        result = {'list_authors': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


    def post(self):
        conn = db_connect.connect()
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        edad = request.json['edad']
        query = conn.execute("INSERT INTO author values('{0}','{1}','{2}')".format(
            nombre,apellido,edad))
        return {'status': 'Author agregado'}
