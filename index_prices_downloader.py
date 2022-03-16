import pandas as pd
import yfinance as yf
import os

# Parameters
start_date     = '1990-01-01'
end_date       = '2022-02-28'
data_interval  = "1d"

# Create a directory where to save .csv files
if not os.path.exists('./index_prices'):
    os.makedirs('./index_prices')

# Download S&P 500 Price Data
sp500_hist = yf.download('^GSPC', start = start_date, end = end_date , data_interval = "1d")
# Download NASDAQ Price Data
nasdaq_hist = yf.download('^IXIC', start = start_date, end = end_date , data_interval = "1d")
# Download CAC40 Price Data
cac40_hist = yf.download('^GSPC', start = start_date, end = end_date , data_interval = "1d")


if __name__ == '__main__':
    sp500_hist.to_csv('./index_prices/SP500.csv', index=True)
    nasdaq_hist.to_csv('./index_prices/NASDAQ.csv', index=True)
    cac40_hist.to_csv('./index_prices/CAC40.csv', index=True)