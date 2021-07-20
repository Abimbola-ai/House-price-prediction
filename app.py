import pickle
from flask import Flask, request, render_template
import numpy as np
import json



app = Flask(__name__)

with open("project/predict_housing_price.pkl", "rb") as f:
    model = pickle.load(f)

def process_input(request_data:str) -> np.array:
    """Takes in the input data and converts it to an array
    that the model can understand"""
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body.shape) == 2, "'Input must be a 2-D array"
    return parsed_body

def error_check()->str:
    """Checks for errors and outputs a string"""
    if (KeyError, json.JSONDecodeError, AssertionError, ValueError):
        return json.dumps({"error": "Check input"}), 400
    else:
        return json.dumps({"error": "Prediction Failed"}), 500

@app.route("/")
def home():
    """Renders the main page to the index template"""
    return render_template('index.html')

@app.route('/predict', methods = ["POST"])
def predict():
    """An interface for the user that plug in the inputs and receive the price
    which is the output"""
    try:
        features =  [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        return render_template("index.html", prediction_text="Predicted House Price is ${}". format(output))
    except:
        return error_check()

@app.route('/results',methods=['POST'])
def results() -> str:
    """User loads the input in a using request and gets 
    the house price without the templates"""
    try:
        input_params = process_input(request.data)
        prediction = model.predict(input_params)
        return json.dumps({"Predicted House Price in Dollars": prediction.tolist()})
    except:
        return error_check()
    

if __name__ == "__main__":
    app.run(debug=True)