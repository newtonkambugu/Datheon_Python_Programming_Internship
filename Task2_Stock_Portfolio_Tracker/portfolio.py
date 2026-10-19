import yfinance as yf
import csv

def load_stock_data(tickers):
    stock_prices = {}
    for ticker in tickers:
        try:
            data=yf.Ticker(ticker)
            current_price=data.history(period="1d")["Close"].iloc[-1]
            stock_prices[ticker]= round(current_price,2)
        except Exception as e:
            print(f"Could not fetch price for {ticker}: {e}")    
    return stock_prices
    


def get_portfolio():
    portfolio = {}
    print("Enter your stock holdings (type 'done' to finish):")
    while True:
        ticker = input("Stock ticker: ").upper()
        if ticker == 'DONE':
            break
        buy_price = float(input("Buy price per share: "))
        quantity = int(input("Number of shares: "))
        portfolio[ticker] = {'buy_price': buy_price, 'quantity': quantity}
    return portfolio


def calculate_performance(portfolio, stock_prices):
    summary = []
    total_invested = 0
    total_value = 0

    for ticker, data in portfolio.items():
        current_price = stock_prices.get(ticker, 0)
        invested = data['buy_price'] * data['quantity']
        value = current_price * data['quantity']
        gain_loss = value - invested
        percent_change = (gain_loss / invested) * 100 if invested != 0 else 0

        summary.append({
            'Ticker': ticker,
            'Buy Price': data['buy_price'],
            'Current Price': current_price,
            'Quantity': data['quantity'],
            'Invested': invested,
            'Value': value,
            'Gain/Loss': gain_loss,
            'Percent Change': percent_change
        })

        total_invested += invested
        total_value += value

    return summary, total_invested, total_value


def save_summary(summary, total_invested, total_value):
    with open('portfolio_summary.csv', 'w', newline='') as file:
        fieldnames = ['Ticker', 'Buy Price', 'Current Price', 'Quantity', 'Invested', 'Value', 'Gain/Loss', 'Percent Change']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary)

    print(f"\nTotal Invested: ${total_invested:.2f}")
    print(f"Current Value: ${total_value:.2f}")
    print(f"Overall Gain/Loss: ${total_value - total_invested:.2f}")


def main():
    portfolio = get_portfolio()
    tickers = list(portfolio.keys())
    stock_prices = load_stock_data(tickers)
    summary, total_invested, total_value = calculate_performance(portfolio, stock_prices)
    save_summary(summary, total_invested, total_value)

if __name__ == "__main__":
    main()
