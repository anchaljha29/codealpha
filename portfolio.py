# portfolio.py
import requests
import json

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol):
        data = self.get_stock_data(symbol)
        if data:
            self.stocks[symbol] = data
            print(f"{symbol} Added to the portfolio.")
        else:
            print(f"Error fetching  for {symbol}.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"{symbol} Removed from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def display_portfolio(self):
        for symbol, data in self.stocks.items():
            last_data_point = next(iter(data["Time Series (1min)"].values()))
            price = last_data_point["4. close"]  
            print(f"{symbol}: {price} USD")

    def get_stock_data(self, symbol):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey=YOUR_API_KEY"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            return None
