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
  carbohydrate = CharField()
  protein = CharField()
  fat = CharField()
  calories = CharField()
  sugar = CharField()
  
db.connect()
db.drop_tables([Fruit])
db.create_tables([Fruit])

apple = Fruit(genus="Malus", name="Apple", family="Rosaceae", order="Rosales", carbohydrate="11.4", protein="0.3", fat="0.4", calories="52", sugar="10.3")
apple.save()
apricot = Fruit(genus="Prunus", name="Apricot", family="Rosaceae", order="Rosales", carbohydrate="3.9", protein="0.5", fat="0.1", calories="15", sugar="3.2")
apricot.save()
banana = Fruit(genus="Musa", name="Banana", family="Musaceae", order="Zingiberales", carbohydrate="22", protein="1", fat="0.2", calories="96", sugar="17.2")
banana.save()
blackberry = Fruit(genus="Rubus", name="Blackberry", family="Rosaceae", order="Rosales", carbohydrate="9", protein="1.3", fat="0.4", calories="40", sugar="4.5")
blackberry.save()
blueberry = Fruit(genus="Fragaria", name="Blueberry", family="Rosaceae", order="Rosales", carbohydrate="5.5", protein="0", fat="0.4", calories="29", sugar="5.4")
blueberry.save()
cherry = Fruit(genus="Prunus", name="Cherry", family="Rosaceae", order="None", carbohydrate="12", protein="1", fat="0.3", calories="50", sugar="8")
cherry.save()
durian = Fruit(genus="Durio", name="Durian", family="Malvaceae", order="Malvales", carbohydrate="27.1", protein="1.5", fat="5.3", calories="147", sugar="6.75")
durian.save()

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

@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
  if request.method == 'GET':
    return jsonify({"message":"Hello, GET"})
  else:
    return jsonify({"message":"Hello, world!"})

app.run(port=9000, debug=True)