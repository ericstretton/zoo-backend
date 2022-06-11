from db_helpers import *
from flask import Flask, Response, jsonify, request 
from flask_cors import CORS




app = Flask(__name__)
animals = []

@app.get('/api/animals')
def animals_get():
    args = request.args
    animal_id = args.get('animalName')
    if animal_id == None:
        return jsonify(animals), 200
    else:
        return jsonify(animals[animal_id]), 200
    

@app.post('/api/animals')
def animals_post():
    animal_data = request.json
    print(animal_data)
    if not animal_data.get('animalName'):
        return jsonify("Missing required field: Animal Name"), 422
    if not animal_data.get('imageURL'):
        return jsonify("Missing required field: imageURL"), 422
    run_query("INSERT INTO user (username, age) VALUES(?,?)", 
        [animal_data.get('animalName'), animal_data.get('animalURL')])

