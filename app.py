
from helpers.db_helpers import run_query
from flask import Flask, jsonify, request 
from flask_cors import CORS
import sys

app = Flask(__name__)


@app.get('/api/animals')
def animals_get():
    # TODO: db select
    animal_list = run_query("SELECT * FROM animal")
    resp = []
    for animal in animal_list:
        an_obj = {}
        an_obj['animalId'] = animal[0]
        an_obj['animalName'] = animal[1]
        an_obj['imageURL'] = animal[2]
        resp.append(an_obj)
    return jsonify(resp), 200
    


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
    
    run_query("INSERT INTO animal (name, image_url) VALUES(?,?)", [animal_name, image_url])
    
    return jsonify("Animal added"), 201
    
    


if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print("Missing required mode argument")
    exit()
if mode == 'testing':
    CORS(app)
    app.run(debug=True)
elif mode == 'production':
    import bjoern
    bjoern.run(app, "0.0.0.0", 5007)
else:
    print("Mode must be in testing|production")
    exit()