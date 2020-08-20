from flask_restful import Resource
from flask import Response, jsonify


categorias=["Ciencias de la Tierra","Economia","Ciencias Politicas","Derecho",
"Informatica","Astronomia","Literatura Universal","Arte y Diseño"]

class categories(Resource):
    def get(self):
        #return {'categorias': [i for i in categorias]}
        return  {'categorias':categorias}
