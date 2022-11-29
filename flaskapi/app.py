from flask import Flask, jsonify, render_template, request
from random import randint
import requests
import json

app = Flask(__name__)


def save_most_recent_pokemon(data):
    with open('most_recent_pokemon.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_most_recent_pokemon():
    with open('most_recent_pokemon.json', 'r') as file:
        return json.load(file)

@app.route('/', methods=['GET'])
def root():
    pokemons = []
    for x in range(6):
        number = str(randint(1,906))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
<<<<<<< HEAD
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)    

=======
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
  
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/gen-one', methods=['GET'])
def gen_one():
    pokemons = []
    for x in range(6):
        number = str(randint(1,151))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
<<<<<<< HEAD

=======
  
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/gen-two', methods=['GET'])
def gen_two():
    pokemons = []
    for x in range(6):
        number = str(randint(152,251))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)

@app.route('/gen-three', methods=['GET'])
def gen_three():
    pokemons = []
    for x in range(6):
        number = str(randint(252, 397))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
<<<<<<< HEAD

=======
 
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/gen-four', methods=['GET'])
def gen_four():
    pokemons = []
    for x in range(6):
        number = str(randint(388, 494))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
<<<<<<< HEAD
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
=======
    
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/gen-five', methods=['GET'])
def gen_five():
    pokemons = []
    for x in range(6):
        number = str(randint(494,650))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
<<<<<<< HEAD

=======
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
  
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/gen-six', methods=['GET'])
def gen_six():
    pokemons = []
    for x in range(6):
        number = str(randint(650,722))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
<<<<<<< HEAD

=======
  
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/gen-seven', methods=['GET'])
def gen_seven():
    pokemons = []
    for x in range(6):
        number = str(randint(722,810))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
<<<<<<< HEAD

=======
  
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/gen-eight', methods=['GET'])
def gen_eight():
    pokemons = []
    for x in range(6):
        number = str(randint(810, 906))
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(baseapi).json()
        data = {
            'number': number,
            'name': resp['name'].upper(),
            'speed': resp['stats'][-1]['base_stat'],
            'defense': resp['stats'][2]['base_stat'],
            'special_defense': resp['stats'][4]['base_stat'],
            'attack': resp['stats'][1]['base_stat'],
            'special_attack': resp['stats'][3]['base_stat'],
            'hp': resp['stats'][0]['base_stat'],
            'weight': resp['weight'],
            'image_url': resp['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(data)
    recent_pokemon_data = load_most_recent_pokemon()
    return render_template('index.html',pokemons=pokemons, recent_pokemon_data=recent_pokemon_data)
<<<<<<< HEAD

=======
  
>>>>>>> bb4ec661b539f2b430d217e1d067032e8e2f1c7d
@app.route('/random-pokemon', methods=['GET'])
def random_pokemon():
    number = str(randint(1,906))
    baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(baseapi).json()
    data = {
        'number': number,
        'name': r['name'].upper(),
        'speed': r['stats'][-1]['base_stat'],
        'defense': r['stats'][2]['base_stat'],
        'special_defense': r['stats'][4]['base_stat'],
        'attack': r['stats'][1]['base_stat'],
        'special_attack': r['stats'][3]['base_stat'],
        'hp': r['stats'][0]['base_stat'],
        'weight': r['weight'],
        'image_url': r['sprites']['other']['dream_world']['front_default']
    }
    save_most_recent_pokemon(data)
    return jsonify(data)


@app.route('/save_recent_pokemon', methods=['POST'])
def save_recent_pokemon():
    request_info = request.get_json(force=True)
    save_most_recent_pokemon(request_info)
    return {'message': 'successful'}

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
