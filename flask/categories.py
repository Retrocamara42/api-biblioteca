from flask_restful import Resource
from flask import Response, jsonify


categorias={
    "Categoria1":"Ciencias de la Tierra",
    "Categoria2":"Economia",
    "Categoria3":"Ciencias Politicas",
    "Categoria4":"Derecho",
    "Categoria5":"Informatica",
    "Categoria6":"Astronomia",
    "Categoria7":"Literatura Universal",
    "Categoria8":"Arte y Diseño"
    }

class categories(Resource):
    def get(self):
        return  categorias
