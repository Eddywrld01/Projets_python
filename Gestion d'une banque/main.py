import os
import json
chemin = os.path.dirname(__file__)
c = os.path.join(chemin,"data")
if not os.path.exists(c):
    os.makedirs(c)
j = os.path.join(c,"banque.json")
with open(j,"w",encoding="utf-8") as f:
    json.dump({"contenu ": "ddd"},f,indent=4)