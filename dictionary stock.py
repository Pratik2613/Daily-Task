# Stock Market Management using Dictionary Operations

def add_stock(stock_data):
    symbol = input("Enter stock symbol: ")
    price = float(input("Enter stock price: "))
    stock_data[symbol] = price
    print("Stock added successfully!\n")

def update_stock(stock_data):
    symbol = input("Enter stock symbol to update: ")
    if symbol in stock_data:
        price = float(input("Enter new stock price: "))
        stock_data[symbol] = price
        print("Stock updated successfully!\n")
    else:
        print("Stock not found!\n")

def remove_stock(stock_data):
    symbol = input("Enter stock symbol to remove: ")
    stock_data.pop(symbol, None)
    print("Stock removed successfully!\n")

def view_stocks(stock_data):
    print("\nCurrent Stock Data:")
    for symbol, price in stock_data.items():
        print(f"{symbol}: ${price}")
    print()

def find_stock(stock_data):
    symbol = input("Enter stock symbol to find: ")
    print("Stock Price:", stock_data.get(symbol, "Stock not found!"))

def copy_stock_data(stock_data):
    return stock_data.copy()

def clear_stocks(stock_data):
    stock_data.clear()
    print("All stocks cleared!\n")

def main():
    stock_data = {}
    while True:
        print("Stock Market Management System")
        print("1. Add Stock")
        print("2. Update Stock")
        print("3. Remove Stock")
        print("4. View Stocks")
        print("5. Find Stock")
        print("6. Copy Stock Data")
        print("7. Clear Stocks")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_stock(stock_data)
        elif choice == '2':
            update_stock(stock_data)
        elif choice == '3':
            remove_stock(stock_data)
        elif choice == '4':
            view_stocks(stock_data)
        elif choice == '5':
            find_stock(stock_data)
        elif choice == '6':
            copied_data = copy_stock_data(stock_data)
            print("Copied Stock Data:", copied_data)
        elif choice == '7':
            clear_stocks(stock_data)
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
