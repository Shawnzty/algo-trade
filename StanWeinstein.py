import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class stan_weinstein():
    def __init__(self, symbol, start, end):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.result = None
        self.get_data()
    
    def get_data(self):
        df = yf.download(self.symbol, start = self.start, end = self.end)
        data = df.Close.to_frame()
        data["Volume"] = df.Volume.to_frame()
        data["Returns"] = np.log(data.Close / data.Close.shift(1))
        data["Close_SMA"] = data.Close.rolling(30*5).mean()
        data["Volume_SMA"] = data.Volume.rolling(5).mean()
        data.dropna(inplace=True)
        self.data = data
        return data
    
    def test_results(self):
        breakout = where(data["Close"] > data["SMA_30"], 1, 0)