# BAD STOCK TRADING APP - DO NOT USE IN REAL LIFE

import random

stocks = {
    "AAPL": 150,
    "GOOG": 2800,
    "TSLA": 720,
    "AMZN": 3400
}

portfolio = {}
money = 10000

def show_menu():
    """
    Display the main menu options for the stock trading application.
    """
    print("1. View Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Exit")

def view_stocks():
    """
    Display the current prices of all stocks, updating each with a random fluctuation.
    
    Each time this function is called, every stock's price is adjusted by a random amount between -100 and 100, simulating market volatility, and the updated prices are printed.
    """
    for stock, price in stocks.items():
        # Prices fluctuate wildly each time you look
        new_price = price + random.randint(-100, 100)
        stocks[stock] = new_price
        print(f"{stock}: ${new_price}")
