# fc24model
Predict the market price of  players based on their stats based on Tensorflow

## Overview

This project utilizes a machine learning model, stored in `best_model.h5`, to predict the prices of players based on their attributes. The environment dependencies are listed in `environment.yml`, and users are encouraged to install them independently.

## Installation

To set up the required environment, use the following command:

```bash
conda env create -f environment.yml
```

## Evaluate Model
Run the following command to check the accuracy of the model predictions, where the maximum prediction error should not exceed 10%.:
```
python evaluate.py
```

## Make Predictions
To make predictions on player prices using their attributes, run:
```
python predict.py
```


## Files
`best_model.h5`: The machine learning model for predicting player prices.
`environment.yml`: Environment dependencies for the project.
`evaluate.py`: Script to evaluate the accuracy of the model.
`predict.py`: Script to predict player prices based on input attributes.
