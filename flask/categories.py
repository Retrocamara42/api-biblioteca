from flask_restful import Resource
from flask import Response, jsonify


categorias=["Ciencias de la Tierra","Economia","Ciencias Politicas","Derecho",
"Informatica","Astronomia","Literatura Universal","Arte y Diseño"]

categorias2=[{"Cat":"Ciencias de la Tierra"},{"Cat":"Economia"},
    {"Cat":"Ciencias Politicas"},{"Cat":"Derecho"},
    {"Cat":"Informatica"},{"Cat":"Astronomia"},{"Cat":"Literatura Universal"},
    {"Cat":"Arte y Diseño"}]

class categories(Resource):
    def get(self):
        #return {'categorias': [i for i in categorias]}
        return  {'categorias':categorias}
