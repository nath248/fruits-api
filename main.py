from flask import Flask
from flask import request
from flask import jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase(
    "fruits", user="postgres", password="", host="localhost", port=5432
)


class BaseModel(Model):
    class Meta:
        database = db


class Fruit(BaseModel):
    genus = CharField()
    name = CharField()
    family = CharField()
    order = CharField()
    carbohydrate = IntegerField()
    protein = IntegerField()
    fat = IntegerField()
    calories = IntegerField()
    sugar = IntegerField()


db.connect()
db.drop_tables([Fruit])
db.create_tables([Fruit])

apple = Fruit(genus="Malus", name="Apple", family="Rosaceae", order="Rosales",
              carbohydrate=11.4, protein=0.3, fat=0.4, calories=52, sugar=10.3)
apple.save()
apricot = Fruit(genus="Prunus", name="Apricot", family="Rosaceae", order="Rosales",
                carbohydrate=3.9, protein=0.5, fat=0.1, calories=15, sugar=3.2)
apricot.save()
banana = Fruit(genus="Musa", name="Banana", family="Musaceae", order="Zingiberales",
               carbohydrate=22, protein=1, fat=0.2, calories=96, sugar=17.2)
banana.save()
blackberry = Fruit(genus="Rubus", name="Blackberry", family="Rosaceae",
                   order="Rosales", carbohydrate=9, protein=1.3, fat=0.4, calories=40, sugar=4.5)
blackberry.save()
blueberry = Fruit(genus="Fragaria", name="Blueberry", family="Rosaceae",
                  order="Rosales", carbohydrate=5.5, protein=0, fat=0.4, calories=29, sugar=5.4)
blueberry.save()
cherry = Fruit(genus="Prunus", name="Cherry", family="Rosaceae",
               order="None", carbohydrate=12, protein=1, fat=0.3, calories=50, sugar=8)
cherry.save()
fig = Fruit(genus="Ficus", name="Fig", family="Moraceae", order="Rosales",
            carbohydrate=19, protein=0.8, fat=0.3, calories=74, sugar=16)
fig.save()
gooseberry = Fruit(genus="Ribes", name="Gooseberry", family="Grossulariaceae",
                   order="Saxifragales", carbohydrate=10, protein=0.9, fat=0.6, calories=44, sugar=0)
gooseberry.save()
grapes = Fruit(genus="Vitis", name="Grapes", family="Vitaceae", order="Vitales",
               carbohydrate=18.1, protein=0.72, fat=0.16, calories=69, sugar=15.48)
grapes.save()
guava = Fruit(genus="Psidium", name="Guava", family="Myrtaceae",
              order="Myrtales", carbohydrate=14, protein=2.6, fat=1, calories=68, sugar=9)
guava.save()

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


@app.route('/genus/<genus>', methods=['GET'])
def genus(genus=None):
    if genus:
        fruit = Fruit.get(Fruit.genus == genus)
        fruit = model_to_dict(fruit)
        return jsonify(fruit)
    else:
        fruits = []
        for fruit in Fruit.select():
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)


@app.route('/name/<name>', methods=['GET'])
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


@app.route('/family/<family>', methods=['GET'])
def family(family=None):
    if family:
        fruit = Fruit.get(Fruit.family == family)
        fruit = model_to_dict(fruit)
        return jsonify(fruit)
    else:
        fruits = []
        for fruit in Fruit.select():
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)


"""
    if family:
        fruits = []
        for family in Fruit.family.select():
            fruit = Fruit.get(Fruit.family == family)
            fruit = model_to_dict(fruit)
            fruits.append(model_to_dict(fruit))
        return jsonify(fruits)
"""


@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello, GET"})
    else:
        return jsonify({"message": "Hello, world!"})


app.run(port=9000, debug=True)
