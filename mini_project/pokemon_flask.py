#!/usr/bin/env python3
from flask import Flask, request, redirect, jsonify, url_for, render_template
import requests
from pprint import pprint

app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/pokemon/<name>", methods=["GET","POST"])
def index(name):
    URL = f"https://pokeapi.co/api/v2/pokemon/{name}"
    resp = requests.get(URL).json()
    pokemon_name = resp["forms"]["name"]
    pokemon_type = resp["types"]["type"]["name"]
    image_url = resp["sprites"]["front-default"]
    
    pokemon_data = []
    pokemon_data.append({"name": pokemon_name, "type": pokemon_type, "image": image_url})
    return jsonify(pokemon_data)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

