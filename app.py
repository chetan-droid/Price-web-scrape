from flask import Flask, jsonify, render_template
from src.service import Price


app = Flask(__name__)


#Create an API 
@app.route('/price', methods=['GET'])
def get_price():
    price = Price.fetch_price()
    if price is not None:
        return render_template('index.html', price=price)
    else:
        return "Could not fetch the price"

@app.route('/',methods= ['GET'])
def home():
    return 'Please use the "URL/price" to get the price'

if __name__ == '__main__':
    app.run()
