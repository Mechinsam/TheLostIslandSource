import json

f = open("test.json", "r")
f = json.load(f)

clas = f["class"]
name = f["name"]
desc = f["desc"]
typ = f["type"]

x = input(f"Choose Catagorey:\n- {clas} ")

if x == clas:
    x = input(f"Choose {clas}:\n- {name} (type:{typ}, {desc}) ")