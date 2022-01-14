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
# db.drop_tables([Fruit])
# db.create_tables([Fruit])

# apple = Fruit(genus="Malus", name="Apple", family="Rosaceae", order="Rosales",
#               carbohydrate=11.4, protein=0.3, fat=0.4, calories=52, sugar=10.3).save()
# apricot = Fruit(genus="Prunus", name="Apricot", family="Rosaceae", order="Rosales",
#                 carbohydrate=3.9, protein=0.5, fat=0.1, calories=15, sugar=3.2).save()
# banana = Fruit(genus="Musa", name="Banana", family="Musaceae", order="Zingiberales",
#                carbohydrate=22, protein=1, fat=0.2, calories=96, sugar=17.2).save()
# blackberry = Fruit(genus="Rubus", name="Blackberry", family="Rosaceae",
#                    order="Rosales", carbohydrate=9, protein=1.3, fat=0.4, calories=40, sugar=4.5).save()
# blueberry = Fruit(genus="Fragaria", name="Blueberry", family="Rosaceae",
#                   order="Rosales", carbohydrate=5.5, protein=0, fat=0.4, calories=29, sugar=5.4).save()
# cherry = Fruit(genus="Prunus", name="Cherry", family="Rosaceae",
#                order="None", carbohydrate=12, protein=1, fat=0.3, calories=50, sugar=8).save()
# fig = Fruit(genus="Ficus", name="Fig", family="Moraceae", order="Rosales",
#             carbohydrate=19, protein=0.8, fat=0.3, calories=74, sugar=16).save()
# gooseberry = Fruit(genus="Ribes", name="Gooseberry", family="Grossulariaceae",
#                    order="Saxifragales", carbohydrate=10, protein=0.9, fat=0.6, calories=44, sugar=0).save()
# grapes = Fruit(genus="Vitis", name="Grapes", family="Vitaceae", order="Vitales",
#                carbohydrate=18.1, protein=0.72, fat=0.16, calories=69, sugar=15.48).save()
# guava = Fruit(genus="Psidium", name="Guava", family="Myrtaceae",
#               order="Myrtales", carbohydrate=14, protein=2.6, fat=1, calories=68, sugar=9).save()

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
