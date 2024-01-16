
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
import pandas as pd

# Load the data
X_train = pd.read_csv("ancestry_train.data", sep=" ", header=None).values
y_train = pd.read_csv("ancestry_train.solution", sep=" ", header=None).values
X_test = pd.read_csv("ancestry_test.data", sep=" ", header=None).values

# Initialize Linear Regression model
linear_reg = LinearRegression()

# Initialize MultiOutputRegressor with Linear Regression
multi_output_linear_reg = MultiOutputRegressor(linear_reg)

# Fit the model
multi_output_linear_reg.fit(X_train, y_train)

# Predict on the test data
predictions = multi_output_linear_reg.predict(X_test)

# Convert predictions to a DataFrame and save as a CSV file
predictions_df = pd.DataFrame(predictions)
predictions_df.to_csv("predictions.csv", sep=" ", header=None, index=None)

# Create a zip file of the predictions.csv
os.system("zip -r predictions.zip predictions.csv")
