from flask import Flask
from flask import request
from flask import jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase(
    "fruit", user="postgres", password="", host="localhost", port=5432
)


class BaseModel(Model):
    class Meta:
        database = db


class Fruit(BaseModel):
    genus = CharField()
    name = CharField()
    family = CharField()
    order_name = CharField()
    carbohydrate = IntegerField()
    protein = IntegerField()
    fat = IntegerField()
    calories = IntegerField()
    sugar = IntegerField()


db.connect()

app = Flask(__name__)


@app.route('/fruit', methods=['GET'])
@app.route('/fruit/<id>', methods=['GET'])
def fruit(id=None):
    if id:
        fruit = Fruit.get(Fruit.id == id)
        fruit = model_to_dict(fruit)
        return jsonify(fruit)
    else:
        fruits = []
        for fruit in Fruit.select():
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)


@app.route('/fruit/genus/<genus>', methods=['GET'])
def genus(genus=None):
    if genus:
        genus_list = []
        for fruit in Fruit.select().where(Fruit.genus == genus):
            genus_list.append(model_to_dict(fruit))
        if len(genus_list) == 0:
            return jsonify({"Error": "Genus not found"})
        else:
            return jsonify(genus_list)
    else:
        fruits = []
        for fruit in Fruit.select():
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)


@app.route('/fruit/name/<name>', methods=['GET'])
def name(name=None):
    if name:
        fruit = Fruit.get(Fruit.name == name)
        fruit = model_to_dict(fruit)
        return jsonify(fruit)
    else:
        fruits = []
        for fruit in Fruit.select():
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)


@app.route('/fruit/family/<family>', methods=['GET'])
def family(family=None):
    if family:
        family_list = []
        for fruit in Fruit.select().where(Fruit.family == family):
            family_list.append(model_to_dict(fruit))
        if len(family_list) == 0:
            return jsonify({"Error": "Family not found"})
        else:
            return jsonify(family_list)
    else:
        fruits = []
        for fruit in Fruit.select():
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)


@app.route('/fruit/order/<order_name>', methods=['GET'])
def order(order_name=None):
    if order_name:
        order_list = []
        for fruit in Fruit.select().where(Fruit.order_name == order_name):
            order_list.append(model_to_dict(fruit))
        if len(order_list) == 0:
            return jsonify({"Error": "Order not found"})
        else:
            return jsonify(order_list)
    else:
        fruits = []
        for fruit in Fruit.select():
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)


@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello, GET"})
    else:
        return jsonify({"message": "Hello, world!"})


app.run(port=9000, debug=True)
