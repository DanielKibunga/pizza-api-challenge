from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the database object
db = SQLAlchemy()
migrate = Migrate()

# This function sets up the app
def create_app():
    app = Flask(__name__)

    # Load settings from config.py
    app.config.from_object("server.config.Config")

    # Connect the database and migration to the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register your routes
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app
