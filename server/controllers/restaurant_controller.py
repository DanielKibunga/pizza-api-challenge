from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models import db

restaurant_bp = Blueprint("restaurant_bp", __name__, url_prefix="/restaurants")

@restaurant_bp.route("/", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

@restaurant_bp.route("/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        data = restaurant.to_dict()
        data["pizzas"] = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
        return jsonify(data), 200
    return jsonify({"error": "Restaurant not found"}), 404

@restaurant_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return "", 204
    return jsonify({"error": "Restaurant not found"}), 404
