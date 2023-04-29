from flask import Flask, jsonify, Response
from project.src.service import Price


def create_app():
    # Create the Flask application
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        return "Please use the /price/ to get the price"

    @app.route('/price/', methods=['GET'])
    def get_price():
        price = Price.fetch_price()
        if price is not None:
            return price
        else:
            return "Could not fetch the price"
        
    return app


