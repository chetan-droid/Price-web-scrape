from flask import Flask, jsonify
from src.service import Price


app = Flask(__name__)


#Create an API 
@app.route('/price', methods=['GET'])
def get_price():
    price = Price.fetch_price()
    if price is not None:
        return price
    else:
        return "Coul not fetch the price"

@app.route('/',methods= ['GET'])
def home():
    return 'Please use the "URL/price" to get the price'

if __name__ == '__main__':
    app.run()
