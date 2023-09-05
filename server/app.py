#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = []
    for bakery in Bakery.query.all():
        bakery_dict = bakery.to_dict()
        
        bakeries.append(bakery_dict)

    response = make_response(
        bakeries,
        200
    )

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()
    print(bakery)
    bakery_dict = bakery.to_dict()
    print(bakery_dict)
    response = make_response( 
        bakery_dict,
        200
    )
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price).all()
    baked_goods_list = []

    baked_goods_fun = []
    for baked_good in baked_goods:
        baked_good_dictionary = baked_good.to_dict()
        baked_goods_fun.append(baked_good_dictionary)
 

    response = make_response(
        baked_goods_fun,
        200
    )
    return response




@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_good = BakedGood.query.order_by(desc(BakedGood.price)).first()
    baked_good_dict = baked_good.to_dict()
    print(f"The baked good dictionary is {baked_good_dict}")
    response = make_response(
        baked_good_dict,
        200
    )


    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
