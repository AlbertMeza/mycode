#!/usr/bin/python3


farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


for farm in farms:
    if farm["name"] == "NE Farm":
        found_it = farm["agriculture"]
        for animal in found_it:
            print(animal)
            break

print()

food = ["carrots", "celery", "apples", "bananas", "oranges"]

for farm in farms:
    print(farm["name"])
choice = input("Pick a farm: ").lower()

for farm in farms:
    if farm["name"].lower() == choice:
        agri = farm["agriculture"]
        for thing in agri:
            if thing not in food:
                print(thing)
        break


