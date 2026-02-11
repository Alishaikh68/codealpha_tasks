
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

total_investment = 0
portfolio = []

print("Available Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter your stock details (type 'done' to finish):")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Try again.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append([stock_name, quantity, investment])

print("\n--- Portfolio Summary ---")
for item in portfolio:
    print(f"Stock: {item[0]}, Quantity: {item[1]}, Investment: ${item[2]}")

print(f"\nTotal Investment Value: ${total_investment}")

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for item in portfolio:
        file.write(f"{item[0]} - Quantity: {item[1]}, Investment: ${item[2]}\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved successfully in 'portfolio.txt'")
