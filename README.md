# Boston House Price Prediction
The project is carried out to fulfill the following requirements:

* Create an API using Flask
* Save and load trained models from the sklearn Boston dataset
* Create inference pipeline for the trained model
* Deploy the Flask application using Heroku

### Features of the dataset:
* CRIM per capita crime rate by town
* ZN proportion of residential land zoned for lots over 25,000 sq.ft.
* INDUS proportion of non-retail business acres per town
* CHAS Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
* NOX nitric oxides concentration (parts per 10 million)
* RM average number of rooms per dwelling
* AGE proportion of owner-occupied units built prior to 1940
* DIS weighted distances to five Boston employment centres
* RAD index of accessibility to radial highways
* TAX full-value property-tax rate per 10,000usd
* PTRATIO pupil-teacher ratio by town
* B 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
* LSTAT % lower status of the population

You can use the app by clicking on the url below:

https://boston-housing-price-app.herokuapp.com/


### For further development:

```
pip install requirements.txt
```

### Below is an example on how to make a price request on 2 inputs:
```
import requests
import json

url = 'http://127.0.0.1:5000/results'
response = requests.post(url, data=json.dumps({"inputs":[[0.00632,28,2.31,1.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98], [0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98]]}))

print(json.loads(response.text))

```
Prints out:
```
{'Predicted House Price in Dollars': [29.175531717632456, 28.994550824582806]}
```