# -*- coding: utf-8 -*-
"""
Wine Tasting.
Author: Ryan Nanson.
"""

# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib


## Load data and first impressions

# Load the dataset
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url)

# Take a first glace at the data
print data.head()

# Fix the fact that the csv was sometimes seperated by semicolons 
data = pd.read_csv(dataset_url, sep=';')
print data.head()

# Look at the dimensions of the data
print data.shape

# Look at the summary statistics
print data.describe()

## Split the data

# Seperate dependent and independent variables
y = data.quality
X = data.drop('quality', axis=1)

# Split data into test and train datasets (80%, 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=123, 
                                                    stratify=y)

