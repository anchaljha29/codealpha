# main.py
from portfolio import Portfolio

def main():
    my_portfolio = Portfolio()
    my_portfolio.add_stock("AAPL")
    my_portfolio.add_stock("MSFT")
    my_portfolio.display_portfolio()
    my_portfolio.remove_stock("AAPL")
    my_portfolio.display_portfolio()

if __name__ == "__main__":
    main()
