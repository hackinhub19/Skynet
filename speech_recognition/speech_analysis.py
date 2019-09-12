from hatesonar import Sonar
import json
sonar = Sonar ()

data = open("data.txt","r")
if data.mode == 'r':
    content = data.read()
    out = sonar.ping(content)
    with open('data.json', 'w') as json_file:
        json.dump(out, json_file)