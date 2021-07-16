import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import json
from werkzeug import serving



app = Flask(__name__)

model = pickle.load(open("predict_housing_price.pkl", "rb"))

def processInput(request_data:str) ->np.array:
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body.shape) == 2, "'Input must be a 2-D array"
    return parsed_body

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods = ["POST"])
def predict():
    try:
        features =  [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        return render_template("index.html", prediction_text="Predicted House Price is ${}". format(output))
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "Check input"}), 400
    except  ValueError:
        return json.dumps({"error": "You cannot input a string"}), 400
    except:
        return json.dumps({"error": "Prediction Failed"}), 500

@app.route('/results',methods=['POST'])
def results() -> str:
    try:
        input_params = processInput(request.data)
        prediction = model.predict(input_params)
        output = round(prediction[0],2)
        return json.dumps({"Predicted House Price in Dollars": output.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "Check input"}), 400
    except  ValueError:
        return json.dumps({"error": "You cannot input a string"}), 400
    except:
        return json.dumps({"error": "Prediction Failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)