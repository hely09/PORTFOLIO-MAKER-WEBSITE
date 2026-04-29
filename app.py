from flask import Flask,jsonify,request
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

stores = [
    {
    'name' : 'flower shop',
    'products' : [{
    'products_name' : 'flowers',
    'product_items' : ['rose', 'lily', 'iris']
    }]
},
{
    'name' : 'fruits shop',
    'products' : [{
    'products_name' : 'fruits',
    'product_items' : ['apple', 'banana', 'cherry']
    }]
}
]

@app.route('/')
def index():
    return "Hello World"

@app.route('/stores', methods=['get'])
def fetch_all_stores():
    return jsonify(stores)

@app.route('/store', methods=['post'])
def add_store():
    req_data = request.get_json()
    data = dict(name=req_data['name'], products=[])
    stores.append(data)
    return jsonify(stores)


# @app.route('/store/<name>', methods=['post'])
# def add_products(name):
#     req_data = request.get_json()
#     for store in stores:
#         if name in store['name']:
#             data = dict(products_name=req_data['name'], product_items=req_data['products'])
#             store['products'].append(data)
#             return jsonify(stores)
#     return jsonify({"message":"store not found"})

@app.route('/store/<name>', methods=['delete'])
def delete_store(name):
    for store in stores:
        if name in store['name']:
            main_name = store['name']
            rest_stores = [el for el in stores if el['name'] != main_name]
            return jsonify(rest_stores)
    return jsonify({"message":"store not found"}) 


@app.route('/store/<name>', methods=['put'])
def update_store(name):
    req_data = request.get_json()
    for store in stores:
        if name in store['name']:
            store['name'] = req_data['name']
            return jsonify(stores)
    return jsonify({"message":"store not found"}) 

@app.route('/store/<name>', methods=['put'])
def update_items(name):
    req_data = request.get_json()
    for store in stores:
        if name in store['name']:
            data = dict(products_name=req_data['products_name'],product_items=req_data['product_items'])
            store['products'] = [data]
            return jsonify(stores)
    return jsonify({"message":"store not found"})


@app.route('/store/<name>')
def fetch_store_by_name(name):
    for store in stores:
        if name in store['name']:
            return jsonify(store)
    return jsonify({"message":"store not found"})


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV')=='devlopment')

































