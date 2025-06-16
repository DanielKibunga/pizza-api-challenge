from server.app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade="all, delete")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "address": self.address}
