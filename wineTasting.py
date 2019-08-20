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
print(data.head)

# Fix the fact that the csv was sometimes seperated by semicolons 
data = pd.read_csv(dataset_url, sep=';')
print(data.head)

# Look at the dimensions of the data
print(data.shape)

# Look at the summary statistics
print(data.describe)

## Split the data

# Seperate dependent and independent variables
y = data.quality
X = data.drop('quality', axis=1)

# Split data into test and train datasets (80%, 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=123, 
                                                    stratify=y)

# Fit the Transformer API
scaler = preprocessing.StandardScaler().fit(X_train)

# Apply the transformer to the training data
X_train_scaled = scaler.transform(X_train)
 
print(X_train_scaled.mean(axis=0))
# Scaled mean, eg:
# [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 
print(X_train_scaled.std(axis=0))
# Scaled std, eg:
# [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]

# Apply the transformer to the test data
X_test_scaled = scaler.transform(X_test)
 
print(X_test_scaled.mean(axis=0))
# [ 0.02776704  0.02592492 -0.03078587 -0.03137977 -0.00471876 -0.04413827
#  -0.02414174 -0.00293273 -0.00467444 -0.10894663  0.01043391]
 
print(X_test_scaled.std(axis=0))
# [ 1.02160495  1.00135689  0.97456598  0.91099054  0.86716698  0.94193125
#  1.03673213  1.03145119  0.95734849  0.83829505  1.0286218 ]

## Notice the test data is transformed using the train data means and so the 
## test data is not exactlyperfectly centered at zero with unit variance.

pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))

# List tuneable hyperparameters 
print(pipeline.get_params())

# Declare hyperparameters we want to tune
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}


## Let's use SckScikit-Learn instead
# Sklearn cross-validation with pipeline:
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
 
# Fit and tune model
clf.fit(X_train, y_train)

# Refit on the entire training set
print(clf.best_params_)
print(clf.refit)

# Evaluate model pipeline on test data
y_pred = clf.predict(X_test)

print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))

# Save model for future use
joblib.dump(clf, 'rf_regressor.pkl')
# To load: clf2 = joblib.load('rf_regressor.pkl')
