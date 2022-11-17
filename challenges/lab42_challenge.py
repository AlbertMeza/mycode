#!/usr/bin/python3

def main():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user"
        :{"awesome": "c", "name":
            {"first": "eyes", "last": "toes"}},
        "banana": 15, "d": "nothing"}]
    
    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[-1]}!")
    trialEyes = trial[2]["goggles"];
    trialGoggles = trial[2]["eyes"];
    trialNothing = trial[-1];
    print(f"My {trialEyes}! The {trialGoggles} do {trialNothing}!")
    nightmareEyes=nightmare[0]["user"]["name"]["first"] 
    nightmareGoggles=nightmare[0]["kumquat"]
    nightmareNothing=nightmare[0]["d"]
    print(f"My {nightmareEyes}! The {nightmareGoggles} do {nightmareNothing}!")
main()
