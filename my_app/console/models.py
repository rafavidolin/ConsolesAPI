from my_app import db


class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))
    active = db.Column(db.Boolean)
    qtdGames = db.Column(db.Integer)

    def __init__(self,name,year,price,active,qtdGames):
        self.name = name
        self.year = year
        self.price = price
        self.active = active
        self.qtdGames = qtdGames

    def __repr__(self):
        return 'Console {0}'.format(self.id)