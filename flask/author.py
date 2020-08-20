from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:////biblioteca.db')

def author(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM author WHERE id=%d " % int(id))
        result = {'author': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
