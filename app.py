import pickle
from flask import Flask, request
import numpy as np
import json

clf = pickle.load(open("predict_housing_price.pkl", "rb"))

app = Flask(__name__)


def processInput(request_data: str) -> np.array:
    input_data = np.asarray(json.loads(request_data)["inputs"])
    assert len(input_data.shape) == 13, "'inputs' must be a 13 dimensional array"
    return input_data

@app.route('/predict', methods = ["POST"])
def predict_housing_price() -> str:
    if request.method == "POST":
        try: 
            input_data = processInput(request.data)
            prediction = clf.predict(input_data)
            return json.dumps({"Predicted House Price :", prediction.tolist()})
        except (KeyError, json.JSONDecodeError, AssertionError):
            return json.dumps({"error": "Check input"}), 400
        except:
            return json.dumps({"error": "Prediction Failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)