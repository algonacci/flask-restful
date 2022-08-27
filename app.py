from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):    
    def get(self, name):
        return {'student_name': name}

    def post(self, name):
        items.append(name)
        return {'student_name': name}

api.prefix = '/api'
api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)