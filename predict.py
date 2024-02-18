import tkinter as tk
import pandas as pd
import math
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import joblib
from util import *


import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
# 创建主窗口
root = tk.Tk()
root.title("输入数据")
namelist=['位置:','花式:','逆足:','速度:','射门:','传球:','盘带:','防守:','身体:','身高:']
# 创建10个输入框
entry_widgets = []
for i in range(10):
    label = tk.Label(root, text=namelist[i])
    label.grid(row=i, column=0, padx=5, pady=5, sticky='e')
    
    entry = tk.Entry(root, width=10)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entry_widgets.append(entry)



def get_inputs():
    inputs = [entry.get() for entry in entry_widgets]
    inputs[0] = pos2num(inputs[0])
    try:
        inputs = [float(value) for value in inputs]
        output_value = ha_function(inputs)
        output_label.config(text=f"预测价格: {output_value}")
    except ValueError:
        output_label.config(text="请输入有效的数字！")
# 创建按钮，点击后获取用户输入
submit_button = tk.Button(root, text="计算价格", command=get_inputs)
submit_button.grid(row=10, column=0, columnspan=2, pady=10)


# 创建标签，用于显示输出值
output_label = tk.Label(root, text="价格: ")
output_label.grid(row=11, column=0, columnspan=2, pady=5)

# 运行主循环
root.mainloop()
