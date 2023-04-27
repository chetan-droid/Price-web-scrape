from flask import Flask, jsonify
from src.service import Price


app = Flask(__name__)


#Create an API 
@app.route('/price', methods=['GET'])
def get_price():
    price = Price.fetch_price()
    if price is not None:
        return jsonify({'price': price})
    else:
        return jsonify({'error': "Could not fetch price"})

@app.route('/',methods= ['GET'])
def home():
    return jsonify({'error': 'Please use the "URL/price" to get the price'})

if __name__ == '__main__':
    app.run(debug=True)
