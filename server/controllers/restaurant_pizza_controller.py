from flask import Blueprint, request, jsonify
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint("restaurant_pizza_bp", __name__, url_prefix="/restaurant_pizzas")

@restaurant_pizza_bp.route("/", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = int(data["price"])
        if price < 1 or price > 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

        rp = RestaurantPizza(
            price=price,
            pizza_id=data["pizza_id"],
            restaurant_id=data["restaurant_id"]
        )
        db.session.add(rp)
        db.session.commit()
        return jsonify(rp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": ["Invalid data"]}), 400