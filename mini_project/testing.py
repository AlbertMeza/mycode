#!/usr/bin/env python3
import requests
from pprint import pprint

URL = "https://pokeapi.co/api/v2/pokemon/ditto"

resp= requests.get(URL).json()

pprint(resp)
