import requests
import json

url = 'http://127.0.0.1:5000/results'
resp = requests.post(url, data=json.dumps({"inputs":[[0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98]]}))

print(json.loads(resp.text))