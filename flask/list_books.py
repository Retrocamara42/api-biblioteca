from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:////biblioteca.db')

class list_books(Resource):
    def get(self):
        conn = db_connect.connect()
        nombre = request.json['nombre']
        autor = request.json['autor']
        query = conn.execute("SELECT * FROM book where autor like '%{0}%' OR nombre='{1}'".format(
            autor,nombre))
        result = {'author': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


    def post(self):
        conn = db_connect.connect()
        nombre = request.json['nombre']
        editorial = request.json['editorial']
        autor = request.json['autor']
        categoria = request.json['categoria']
        query = conn.execute("INSERT INTO book values('{0}','{1}','{2}','{4}')".format(
            nombre,editorial,autor,categoria))
        return {'status': 'Libro agregado'}
