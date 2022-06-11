from cProfile import run
from helpers.db_helpers import run_query
from flask import Flask, jsonify, request 

app = Flask(__name__)
animals = []

@app.get('/api/animals')
def animals_get():
    # TODO: db select
    animal_list = run_query()
    return jsonify(animal_list), 200
    
    

@app.post('/api/animals')
def animals_post():
    data = request.json
    animal_name = data.get('animalName')
    image_url = data.get('imageURL')
    if not animal_name:
        return jsonify("Missing required argument: animalName"), 422
    if not image_url:
        return jsonify("Missing required field: imageURL"), 422
    # TODO: Error checking the actual values for the arguments
    
    # TODO: DB write
    
    # run_query("INSERT INTO animal (animalName, imageURL) VALUES(?,?)", 
    #     [data.get('animalName'), data.get('animalURL')])

