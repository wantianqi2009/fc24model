import pandas as pd
import math
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import joblib
import matplotlib.pyplot as plt


def getptp(linenumber,dataset,model,loaded_scaler):
    first_row = dataset.iloc[linenumber, 2:12].values
    h=np.array([first_row])
    scaled_first_row = loaded_scaler.transform(h)
    #predicted_prices = np.expm1(model.predict(scaled_first_row))
    pp=model.predict(scaled_first_row,verbose=None)
    tp=np.log1p(dataset.iloc[linenumber, 1])
    #return np.expm1(pp),np.expm1(tp)
    return pp,tp

def pos2num(position):
    positions = {
        'ST': 1,
        'CF': 2,
        'LW': 4,
        'RW': 4,
        'LM': 4,
        'RM': 4,
        'CAM': 3,
        'CDM': 6,
        'CM': 5,
        'LB': 7,
        'RB': 7,
        'LWB': 7,
        'RWB': 7,
        'CB': 8,
        'GK': 9,
    }
    
    position = position.strip().upper()  # 去除首尾空格并转换为大写
    
    if position not in positions:
        raise ValueError('请输入正确的位置')
    
    return positions[position]


###将价格转换为M，K
def mapprice(mapped_price):
    if mapped_price >= 1000000:
        finalprice=str(round(mapped_price/1000000,2))+'M'
    elif 1000 <= mapped_price < 1000000:
        finalprice=str(round(mapped_price/1000,2))+'K'
    return finalprice


##预测价格
def ha_function(inputs):
    h = np.array([inputs])
    model = load_model('best_model.h5')
    loaded_scaler = joblib.load('scaler_model.pkl')
    scaled_first_row = loaded_scaler.transform(h)
    predicted_prices = np.expm1(model.predict(scaled_first_row))
    finalprice=mapprice(predicted_prices[0][0])
    return finalprice


