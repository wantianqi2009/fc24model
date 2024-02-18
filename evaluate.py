import pandas as pd
import math
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import joblib
import matplotlib.pyplot as plt
from util import *

model = load_model('best_model.h5')
loaded_scaler = joblib.load('scaler_model.pkl')
data = pd.read_csv('backup.csv', encoding='ISO-8859-1')

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")



pplist=[]
tplist=[]
errorlist=[]
for i in range(data.shape[0]):
    pp,tp=getptp(i,data,model,loaded_scaler)
    error=abs(pp-tp)/tp
    pplist.append(pp)
    tplist.append(tp)
    errorlist.append(error[0][0])

maxerror=round(max(errorlist)*100,2)


plt.figure(figsize=(6, 6))
plt.scatter(pplist, tplist, label='True vs Predicted', marker='o')
plt.plot([min(pplist)[0][0], max(pplist)[0][0]], [min(pplist)[0][0], max(pplist)[0][0]], '--', label='Perfect Prediction')
plt.xlabel('Predicted Prices (log scale)')
plt.ylabel('True Prices (log scale)')
plt.text(0.5, 0.9, f'Max Error: {maxerror}%', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.legend(loc='lower right')
plt.show()