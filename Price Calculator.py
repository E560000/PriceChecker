print("CeX Profit Checker (No support for colour)")
category = input("Enter Category (Apple Watch), (iPod Classic): ")

if category == "iPod Classic":
    print("iPod Classic selected. (7th gen is 6.160.09)")
    # Define the base prices for models
    b_base_prices = {
        "1.5": 19,
        "1.10": 22,
        "2.10": 25,
        "2.20": 29,
        "3.10": 21,
        "3.15": 25,
        "3.20": 33,
        "3.30": 35,
        "3.40": 37,
        "4.20": 28,
        "4.30": 38,
        "4.u2": 34,
        "4.40": 37,
        "4.60": 41,
        "5.30": 42,
        "5.60": 48,
        "5.80": 45,
        "6.80": 55,
        "6.120": 57,
        "6.160": 65,
        "6.160.09": 74
    }
    
    c_base_prices = {
        "1.5": 17,
        "1.10": 18,
        "2.10": 19,
        "2.20": 25,
        "3.10": 19,
        "3.15": 21,
        "3.20": 31,
        "3.30": 33,
        "3.40": 33,
        "4.20": 25,
        "4.30": 25,
        "4.u2": 29,
        "4.40": 31,
        "4.60": 35,
        "5.30": 29,
        "5.60": 25,
        "5.80": 37,
        "6.80": 34,
        "6.120": 42,
        "6.160": 42,
        "6.160.09": 45
    }
    while True:
        shipping = float(input("Input shipping price: "))
        model = input("Enter model (1-7, 4.u2) with decimal point to indicate storage or 'exit' to quit: ")
        if model.lower() == 'exit':
            break
        
        if model not in b_base_prices:
            print("Invalid model. Please enter a model between 1-7 and a decimal for storage.")
            continue

        price = input("Enter price: ")
        try:
            price = float(price)  # Convert price to float
        except ValueError:
            print("Invalid price input. Please enter a numeric value.")
            continue
        
        condition = input("Enter condition (b/c): ")
        if condition not in ['b', 'c']:
            print("Invalid condition. Please enter 'b' or 'c'.")
            continue
        
        # Calculate profit
        if condition == 'b':
            base_price = b_base_prices[model]
            profit = (base_price - price) - shipping
        else:  # condition 'c'
            base_price = c_base_prices[model]
            profit = (base_price - price) - shipping
        
        print(f"Profit for model {model} (condition '{condition}'): {profit:.2f}")

if category == "Apple Watch":
    print("Apple Watch selected")
    # Define the base prices for models
    b_base_prices = {
        "1": 23,
        "2": 23,
        "3": 31,
        "4": 45,
        "5": 57,
        "6": 68,
        "7": 74,
        "8": 108,
        "9": 140,
        "10": 188,
        "SE1": 54,
        "SE2": 71
    }
    c_base_prices = {
        "1": 18,
        "2": 20,
        "3": 23,
        "4": 34,
        "5": 38,
        "6": 45,
        "7": 57,
        "8": 76,
        "9": 115,
        "10": 182,
        "SE1": 37,
        "SE2": 45 
    }

    while True:
        shipping = float(input("Input shipping price: "))
        model = input("Enter model (1-10, SE1, SE2) or 'exit' to quit: ")
        if model.lower() == 'exit':
            break
        
        if model not in b_base_prices:
            print("Invalid model. Please enter a model between 1-10 or SE1/SE2.")
            continue

        price = input("Enter price: ")
        try:
            price = float(price)  # Convert price to float
        except ValueError:
            print("Invalid price input. Please enter a numeric value.")
            continue
        
        condition = input("Enter condition (b/c): ")
        if condition not in ['b', 'c']:
            print("Invalid condition. Please enter 'b' or 'c'.")
            continue
        
        # Calculate profit
        if condition == 'b':
            base_price = b_base_prices[model]
            profit = (base_price - price) - shipping
        else:  # condition 'c'
            base_price = c_base_prices[model]
            profit = (base_price - price) - shipping
        
        print(f"Profit for model {model} (condition '{condition}'): {profit:.2f}")

else:
    print("Invalid category selected.")
