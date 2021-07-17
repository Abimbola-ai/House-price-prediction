import json
from app import *

def test_home(app, client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict(app, client):
    response = app.test_client().post("/results",data=json.dumps({"inputs":[[0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98]]}),
    content_type="application/json") 
    assert response.status_code == 200
    assert response.data == b'{"Predicted House Price in Dollars": 28.99}'
