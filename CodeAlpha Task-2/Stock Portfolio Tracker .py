import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "GOOGL": 140.20,
    "MSFT": 320.90,
    "AMZN": 130.40,
    "NVDA": 450.10,
    "DIS": 85.60,
    "SBUX": 95.30
}

def get_portfolio_input():
    
    portfolio = {}
    print("\n--- Available Tickers ---")
    print(", ".join(STOCK_PRICES.keys()))
    print("-------------------------")

    while True:
        
        ticker = input("\nEnter stock ticker (e.g., AAPL) or type 'done' to finish: ").upper().strip()

        if ticker == 'DONE':
            break

        if ticker not in STOCK_PRICES:
            print(f"Error: '{ticker}' not found in the hardcoded prices. Please try again or type 'done'.")
            continue

        
        try:
            quantity_str = input(f"Enter quantity for {ticker}: ")
            quantity = int(quantity_str)
            if quantity <= 0:
                print("Error: Quantity must be a positive integer.")
                continue
           
            portfolio[ticker] = portfolio.get(ticker, 0) + quantity
            print(f"Added {quantity} shares of {ticker}. Current total shares: {portfolio[ticker]}")

        except ValueError:
            print("Error: Invalid quantity. Please enter a whole number.")
            
    return portfolio

def calculate_investment_value(portfolio, prices):
    """
    Calculates the total value for the given portfolio based on the current prices.
    Returns (total_value, detailed_breakdown)
    """
    total_value = 0.0
    detailed_breakdown = []
    
    for ticker, quantity in portfolio.items():
        price = prices.get(ticker, 0) 
        
        if price > 0:
            current_value = quantity * price
            total_value += current_value
            detailed_breakdown.append({
                "ticker": ticker,
                "quantity": quantity,
                "price": price,
                "value": current_value
            })
            
    return total_value, detailed_breakdown

def save_results_to_file(total_value, breakdown):
    """
    Saves the portfolio summary and total value to a plain text file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_summary_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as f:
            f.write("--- Stock Portfolio Tracker Summary ---\n")
            f.write(f"Date Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("Portfolio Holdings:\n")
            f.write("-" * 40 + "\n")
            f.write(f"{'Ticker':<10}{'Quantity':<10}{'Price':<10}{'Value':>10}\n")
            f.write("-" * 40 + "\n")
            
            for item in breakdown:
                line = (
                    f"{item['ticker']:<10}"
                    f"{item['quantity']:<10}"
                    f"${item['price']:<9.2f}"
                    f"${item['value']:>9.2f}"
                )
                f.write(line + "\n")
            
            f.write("-" * 40 + "\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}\n")
            f.write("-" * 40 + "\n")
            
        print(f"\nSuccess! Results saved to {filename}")
        
    except Exception as e:
        print(f"\nError: Could not save file. Reason: {e}")

def main():
   
    print("Welcome to the Simple Stock Portfolio Tracker!")
    
    portfolio = get_portfolio_input()
    
    if not portfolio:
        print("\nNo stocks entered. Exiting the tracker.")
        return

    total_value, breakdown = calculate_investment_value(portfolio, STOCK_PRICES)
    
    print("\n" + "="*50)
    print("   *** PORTFOLIO VALUATION REPORT ***")
    print("="*50)
    
    print(f"{'Stock':<10} {'Shares':<8} {'Price':>10} {'Value':>12}")
    print("-" * 50)
    for item in breakdown:
        print(
            f"{item['ticker']:<10} "
            f"{item['quantity']:<8} "
            f"${item['price']:>9.2f} "
            f"${item['value']:>11,.2f}"
        )
    print("-" * 50)
    print(f"TOTAL MARKET VALUE: ${total_value:,.2f}")
    print("="*50)

    save_option = input("\nDo you want to save this summary to a text file? (y/n): ").strip().lower()
    if save_option == 'y':
        save_results_to_file(total_value, breakdown)
    
    print("\nThank you for using the Stock Tracker!")

if __name__ == "__main__":
    main()
