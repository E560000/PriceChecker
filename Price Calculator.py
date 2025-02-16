print("CeX Profit Checker (No support for colour)")
category = input("Enter Category (Apple Watch), (iPod Classic), (iPhone): ")

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

elif category == "Apple Watch":
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

elif category == "iPhone":
    print("iPhone selected, no support for network provider.")
    # Define the base prices for models
    a_base_prices = {
        "4.8"=
        "4.16"=
        "4.32"=
        "4s.8"=
        "4s.16"=
        "4s.32"=
        "4s.64"=
        "5.16"=
        "5.32"=
        "5.64"=
        "5c.8"=
        "5c.16"=
        "5c.32"=
        "6.16"=
        "6.32"=
        "6.64"=
        "6.128"=
        "6s.16"=
        "6s.32"=
        "6s.64"=
        "6s.128"=
        "6sPlus.16"=
        "6sPlus.32"=
        "6sPlus.64"=
        "6sPlus.128"=
        "SE1.16"=
        "SE1.32"=
        "SE1.64"=
        "SE1.128"=
        "7.32"=
        "7.128"=
        "7.256"=
        "7Plus.32"=
        "7Plus.128"=
        "7Plus.256"=
        "8.64"=
        "8.128"=
        "8.256"=
        "8Plus.64"=
        "8Plus.128"=
        "8Plus.256"=
        "x.64"=
        "x.256"=
        "xs.64"=
        "xs.256"=
        "xs.512"=
        "xsMax.64"=
        "xsMax.256"=
        "xsMax.512"=
        "xr.64"=
        "xr.128"=
        "xr.256"=
        "11.64"=
        "11.128"=
        "11.256"=
        "11Pro.64"=
        "11Pro.256"=
        "11Pro.512"=
        "11ProMax.64"=
        "11ProMax.256"=
        "11ProMax.512"=
        "SE2.64"=
        "SE2.128"=
        "SE2.256"=
        "12.64"=
        "12.128"=
        "12.256"=
        "12Mini.64"=
        "12Mini.128"=
        "12Mini.256"=
        "12Pro.128"=
        "12Pro.256"=
        "12Pro.512"=
        "12ProMax.128"=
        "12ProMax.256"=
        "12ProMax.512"=
        "13.128"=
        "13.256"=
        "13.512"=
        "13Mini.128"=
        "13Mini.256"=
        "13Mini.512"=
        "13Pro.128"=
        "13Pro.256"=
        "13Pro.512"=
        "13Pro.1024"=
        "13ProMax.128"=
        "13ProMax.256"=
        "13ProMax.512"=
        "13ProMax.1024"=
        "SE3.64"=
        "SE3.128"=
        "SE3.256"=
        "14.128"= 
        "14.256"=
        "14.512"=
        "14Plus.128"=
        "14Plus.256"=
        "14Plus.512"=
        "14Pro.128"=
        "14Pro.256"=
        "14Pro.512"=
        "14Pro.1024"=
        "14ProMax.128"=
        "14ProMax.256"=
        "14ProMax.512"=
        "14ProMax.1024"=
        "15.128"=
        "15.256"=
        "15.512"=
        "15Plus.128"=
        "15Plus.256"=
        "15Plus.512"=
        "15Pro.128"=
        "15Pro.256"=
        "15Pro.512"=
        "15Pro.1024"=
        "15ProMax.256"=
        "15ProMax.512"=
        "15ProMax.1024"=
        "16.128"=
        "16.256"=
        "16.512"=
        "16Plus.128"=
        "16Plus.256"=
        "16Plus.512"=
        "16Pro.128"=
        "16Pro.256"=
        "16Pro.512"=
        "16Pro.1024"=
        "16ProMax.256"=
        "16ProMax.512"=
        "16ProMax.1024"=
        
        
        
        
    }
    b_base_prices = {
           
    }
    c_base_prices = {
               
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
