from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from list_authors import list_authors
from list_books import list_books
from author import author
from book import book
from categories import categories


app = Flask(__name__)
api = Api(app)


api.add_resource(list_authors, '/author')
api.add_resource(list_books, '/book')
api.add_resource(book, '/book/<id>')
api.add_resource(categories, '/categorias')
#api.add_resource(author, '/author/<id>')


if __name__ == '__main__':
     app.run(port='5000')
