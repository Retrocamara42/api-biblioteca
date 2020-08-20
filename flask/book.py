from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:////biblioteca.db')

class book(Resource):
    def get(self,id):
        conn = db_connect.connect()
        query = conn.execute("SELECT nombre,categoria FROM book \
            WHERE  id=%d " % int(id))
        result = {'book': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


    def delete(self,id):
        conn = db_connect.connect()
        query = conn.execute("DELETE FROM author WHERE id= %d " % int(author_id))
        return {'status': 'Libro eliminado'}


    def patch(self,id):
        conn = db_connect.connect()
        nombre = request.json['nombre']
        editorial = request.json['editorial']
        query = conn.execute("UPDATE author SET nombre='%s',editorial='%s' \
            WHERE id= %d " % (nombre,editorial,int(author_id)))
        return {'status': 'Libro eliminado'}
