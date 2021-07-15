"""
A simple regression analysis on the Boston housing data
========================================================

Here we perform a simple regression analysis on the Boston housing
data, exploring two types of regressors.

"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Load data
data = load_boston()

# Data split
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

# Fit train set
clf = GradientBoostingRegressor()
clf.fit(X_train, y_train)

# Predict test set
predicted = clf.predict(X_test)
expected = y_test

# Check metrics
print("RMS: %r " % np.sqrt(np.mean((predicted - expected) ** 2)))

# Dump model ina pickle file
with open("predict_housing_price.pkl", "wb") as f:
    pickle.dump(clf,f)
