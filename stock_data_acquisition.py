import numpy as np
import pandas as pd

import pandas_datareader as pdr

import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns

# ENTER YOUR SETTINGS HERE
stock_ticker = ['CCL','RCL','NCLH']
start_date = '2021-01-01'
end_date = '2021-03-31'

i = 0

while(i < len(stock_ticker)):
    # Get the stock dataframe
    df_stock = pdr.DataReader(stock_ticker[i],
                              data_source='yahoo',
                              start=start_date,
                              end=end_date)

    # Reset the index column
    df_stock.reset_index(inplace=True)

    stock_filepath = 'data/stock_history/stock_' + stock_ticker[i] + '_history.csv'

    # Save stock dataframe to .csv file
    df_stock.to_csv(stock_filepath)

    i += 1
