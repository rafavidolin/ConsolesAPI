import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.console.models import Console
from my_app import api, db

console = Blueprint('console',__name__)

parser = reqparse.RequestParser()
parser.add_argument('name',type=str)
parser.add_argument('year',type=int)
parser.add_argument('price',type=float)

@console.route("/")
@console.route("/home")
def home():
    return "Catálogo de Consoles"

class ConsoleAPI(Resource):
    def get(self,id=None,page=1):
        if not id:
            consoles = Console.query.paginate(page,10).items
        else:
            consoles = [Console.query.get(id)]
        if not consoles:
            abort(404)
        res = {}
        for con in consoles:
            res[con.id] = {
                'name' : con.name,
                'year' : con.year,
                'price' : str(con.price)
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        name = args['name']
        year = args['year']
        price = args['price']

        con = Console(name,year,price)
        db.session.add(con)
        db.session.commit()
        res = {}
        res[con.id] = {
                'name' : con.name,
                'year' : con.year,
                'price' : str(con.price)
        }
        return json.dumps(res)

api.add_resource(
    ConsoleAPI,
    '/api/console',
    '/api/console/<int:id>',
    '/api/console/<int:id>/<int:page>'
)