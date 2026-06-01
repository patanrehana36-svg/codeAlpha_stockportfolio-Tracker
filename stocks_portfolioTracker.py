stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

stock = input("Enter Stock Name: ").upper()
qty = int(input("Enter Quantity: "))

if stock in stocks:
    total = stocks[stock] * qty
    print("Total Investment Value =", total)
else:
    print("Stock Not Found")