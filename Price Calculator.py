print("CeX Profit Checker (No support for colour)\nPlease write model numbers as (ModelName).(StorageSize) e.g 16ProMax.512 for an iphone 16 Pro Max with 512GB storage.\nPrices will be minimum prices, they vary by colour.\nMade by Enis Bayram")
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
        "4.8": 9,
        "4.16": 10,
        "4.32": 10,
        "4s.8": 9,
        "4s.16": 11,
        "4s.32": 10,
        "4s.64": 11,
        "5.16": 11,
        "5.32": 11,
        "5.64": 12,
        "5s.16": 9,
        "5s.32": 11,
        "5s.64": 12,
        "5c.8": 9,
        "5c.16": 9,
        "5c.32": 12,
        "6.16": 11,
        "6.32": 11,
        "6.64": 14,
        "6.128": 14,
        "6s.16": 13,
        "6s.32": 14,
        "6s.64": 14,
        "6s.128": 14,
        "6sPlus.16": 18,
        "6sPlus.32": 19,
        #finally reached £20 XD
        "6sPlus.64": 21,
        "6sPlus.128": 21,
        #also, what is up with this pricing... it's £155 to buy the 128GB version but they take them for £21??
        "SE1.16": 26,
        "SE1.32": 28,
        "SE1.64": 36,
        "SE1.128": 35,
        "7.32": 26,
        "7.128": 28,
        "7.256": 30,
        "7Plus.32": 34,
        "7Plus.128": 39,
        "7Plus.256": 43,
        "8.64": 32,
        "8.128": 36,
        "8.256": 43,
        #okay now they're suddenly valuable :think:
        "8Plus.64": 92,
        "8Plus.128": 101,
        "8Plus.256": 110,
        "x.64": 105,
        "x.256": 112,
        "xs.64": 85,
        "xs.256": 92,
        "xs.512": 98,
        "xsMax.64": 89,
        "xsMax.256": 106,
        "xsMax.512": 115,
        "xr.64": 103,
        "xr.128": 112,
        "xr.256": 119,
        "11.64": 132,
        "11.128": 153,
        "11.256": 173,
        "11Pro.64": 129,
        "11Pro.256": 157,
        "11Pro.512": 166,
        "11ProMax.64": 137,
        "11ProMax.256": 164,
        "11ProMax.512": 175,
        "SE2.64": 90,
        "SE2.128": 96,
        "SE2.256": 103,
        "12.64": 159,
        "12.128": 164,
        "12.256": 175,
        "12Mini.64": 121,
        "12Mini.128": 144,
        "12Mini.256": 144,
        "12Pro.128": 182,
        "12Pro.256": 198,
        "12Pro.512": 225,
        "12ProMax.128": 207,
        "12ProMax.256": 213,
        "12ProMax.512": 234,
        "13.128": 198,
        "13.256": 200,
        "13.512": 220,
        "13Mini.128": 153,
        "13Mini.256": 186,
        "13Mini.512": 231,
        "13Pro.128": 193,
        "13Pro.256": 234,
        "13Pro.512": 249,
        "13Pro.1024": 254,
        "13ProMax.128": 234,
        "13ProMax.256": 267,
        "13ProMax.512": 283,
        "13ProMax.1024": 290,
        "SE3.64": 117,
        "SE3.128": 128,
        "SE3.256": 164,
        "14.128": 225,
        "14.256": 238,
        "14.512": 263,
        "14Plus.128": 247,
        "14Plus.256": 270,
        "14Plus.512": 281,
        "14Pro.128": 258,
        "14Pro.256": 299,
        "14Pro.512": 319,
        "14Pro.1024": 357,
        "14ProMax.128": 385,
        "14ProMax.256": 412,
        "14ProMax.512": 453,
        "14ProMax.1024": 481,
        "15.128": 330,
        "15.256": 368,
        "15.512": 440,
        "15Plus.128": 297,
        "15Plus.256": 333,
        "15Plus.512": 393,
        "15Pro.128": 398,
        "15Pro.256": 437,
        "15Pro.512": 481,
        "15Pro.1024": 550,
        "15ProMax.256": 492,
        "15ProMax.512": 522,
        "15ProMax.1024": 550,
        "16.128": 398,
        "16.256": 440,
        "16.512": 508,
        "16Plus.128": 366,
        "16Plus.256": 393,
        "16Plus.512":461, 
        "16Pro.128": 481,
        "16Pro.256": 522,
        "16Pro.512": 605,
        "16Pro.1024": 687,
        "16ProMax.256": 577,
        "16ProMax.512": 632,
        "16ProMax.1024": 742
        
        
        
        
    }
    b_base_prices = {
        "4.8": 6,
        "4.16": 8,
        "4.32": 8,
        "4s.8": 8,
        "4s.16": 9,
        "4s.32": 8,
        "4s.64": 9,
        "5.16": 9,
        "5.32": 10,
        "5.64": 10,
        "5c.8": 8,
        "5c.16": 9,
        "5c.32": 10,
        "5s.16": 8,
        "5s.32": 9,
        "5s.64": 8,
        "6.16": 8,
        "6.32": 9,
        "6.64": 10,
        "6.128": 11,
        "6s.16": 9,
        "6s.32": 10,
        "6s.64": 9,
        "6s.128": 11,
        "6sPlus.16": 14,
        "6sPlus.32": 15,
        "6sPlus.64": 17,
        "6sPlus.128": 16,
        "SE1.16": 21,
        "SE1.32": 24,
        "SE1.64": 28,
        "SE1.128": 29,
        "7.32": 17,
        "7.128": 20,
        "7.256": 24,
        "7Plus.32": 23,
        "7Plus.128": 28, 
        "7Plus.256": 33,
        "8.64": 25,
        "8.128": 27,
        "8.256": 29,
        "8Plus.64": 65,
        "8Plus.128": 65,
        "8Plus.256": 74,
        "x.64": 81,
        "x.256": 92,
        "xs.64": 61,
        "xs.256": 70,
        "xs.512": 80,
        "xsMax.64": 71,
        "xsMax.256": 87,
        "xsMax.512": 94,
        "xr.64": 72,
        "xr.128": 87,
        "xr.256": 92,
        "11.64": 101,
        "11.128": 117,
        "11.256": 130,
        "11Pro.64": 117,
        "11Pro.256": 132,
        "11Pro.512": 144,
        "11ProMax.64": 114,
        "11ProMax.256": 135,
        "11ProMax.512": 148,
        "SE2.64": 63,
        "SE2.128": 72,
        "SE2.256": 81,
        "12.64": 126,
        "12.128": 127,
        "12.256": 146,
        "12Mini.64": 110,
        "12Mini.128": 117,
        "12Mini.256": 135,
        "12Pro.128": 148,
        "12Pro.256": 164,
        "12Pro.512": 177,
        "12ProMax.128": 177,
        "12ProMax.256": 180,
        "12ProMax.512": 195,
        "13.128": 159,
        "13.256": 180,
        "13.512": 207,
        "13Mini.128": 137,
        "13Mini.256": 162,
        "13Mini.512": 211,
        "13Pro.128": 180,
        "13Pro.256": 202,
        "13Pro.512": 216,
        "13Pro.1024": 220,
        "13ProMax.128": 209,
        "13ProMax.256": 236,
        "13ProMax.512": 249,
        "13ProMax.1024": 258,
        "SE3.64": 96,
        "SE3.128": 117,
        "SE3.256": 148,
        "14.128": 189,
        "14.256": 216,
        "14.512": 240,
        "14Plus.128": 202,
        "14Plus.256": 236,
        "14Plus.512": 258,
        "14Pro.128": 231,
        "14Pro.256": 272,
        "14Pro.512": 292,
        "14Pro.1024": 330,
        "14ProMax.128": 324,
        "14ProMax.256": 343,
        "14ProMax.512": 385,
        "14ProMax.1024": 407,
        "15.128": 291,
        "15.256": 341,
        "15.512": 412,
        "15Plus.128": 279,
        "15Plus.256": 315,
        "15Plus.512": 371,
        "15Pro.128": 365,
        "15Pro.256": 412,
        "15Pro.512": 451,
        "15Pro.1024": 514,
        "15ProMax.256": 440,
        "15ProMax.512": 473,
        "15ProMax.1024": 508,
        "16.128": 376,
        "16.256": 418, 
        "16.512": 481,
        "16Plus.128": 348,
        "16Plus.256": 371,
        "16Plus.512": 434,
        "16Pro.128": 453,
        "16Pro.256": 495,
        "16Pro.512": 572,
        "16Pro.1024": 649,
        "16ProMax.256": 550,
        "16ProMax.512": 591,
        "16ProMax.1024": 701
    }
    c_base_prices = {
        "4.8": 
        "4.16": 
        "4.32": 
        "4s.8": 
        "4s.16": 
        "4s.32": 
        "4s.64": 
        "5.16": 
        "5.32": 
        "5.64": 
        "5c.8": 
        "5c.16": 
        "5c.32": 
        "5s.16": 
        "5s.32": 
        "5s.64": 
        "6.16": 
        "6.32": 
        "6.64": 
        "6.128": 
        "6s.16": 
        "6s.32": 
        "6s.64": 
        "6s.128": 
        "6sPlus.16": 
        "6sPlus.32": 
        "6sPlus.64": 
        "6sPlus.128": 
        "SE1.16": 
        "SE1.32": 
        "SE1.64": 
        "SE1.128": 
        "7.32": 
        "7.128": 
        "7.256": 
        "7Plus.32": 
        "7Plus.128": 
        "7Plus.256": 
        "8.64": 
        "8.128": 
        "8.256": 
        "8Plus.64": 
        "8Plus.128": 
        "8Plus.256": 
        "x.64": 
        "x.256": 
        "xs.64": 
        "xs.256": 
        "xs.512": 
        "xsMax.64": 
        "xsMax.256": 
        "xsMax.512": 
        "xr.64": 
        "xr.128": 
        "xr.256": 
        "11.64": 
        "11.128": 
        "11.256": 
        "11Pro.64": 
        "11Pro.256": 
        "11Pro.512": 
        "11ProMax.64": 
        "11ProMax.256": 
        "11ProMax.512": 
        "SE2.64": 
        "SE2.128": 
        "SE2.256": 
        "12.64": 
        "12.128": 
        "12.256": 
        "12Mini.64": 
        "12Mini.128": 
        "12Mini.256": 
        "12Pro.128": 
        "12Pro.256": 
        "12Pro.512": 
        "12ProMax.128": 
        "12ProMax.256": 
        "12ProMax.512": 
        "13.128": 
        "13.256": 
        "13.512": 
        "13Mini.128": 
        "13Mini.256": 
        "13Mini.512": 
        "13Pro.128": 
        "13Pro.256": 
        "13Pro.512": 
        "13Pro.1024": 
        "13ProMax.128": 
        "13ProMax.256": 
        "13ProMax.512": 
        "13ProMax.1024": 
        "SE3.64": 
        "SE3.128": 
        "SE3.256": 
        "14.128":  
        "14.256": 
        "14.512": 
        "14Plus.128": 
        "14Plus.256": 
        "14Plus.512": 
        "14Pro.128": 
        "14Pro.256": 
        "14Pro.512": 
        "14Pro.1024": 
        "14ProMax.128": 
        "14ProMax.256": 
        "14ProMax.512": 
        "14ProMax.1024": 
        "15.128": 
        "15.256": 
        "15.512": 
        "15Plus.128": 
        "15Plus.256": 
        "15Plus.512": 
        "15Pro.128": 
        "15Pro.256": 
        "15Pro.512": 
        "15Pro.1024": 
        "15ProMax.256": 
        "15ProMax.512": 
        "15ProMax.1024": 
        "16.128": 
        "16.256": 
        "16.512": 
        "16Plus.128": 
        "16Plus.256": 
        "16Plus.512": 
        "16Pro.128": 
        "16Pro.256": 
        "16Pro.512": 
        "16Pro.1024": 
        "16ProMax.256": 
        "16ProMax.512": 
        "16ProMax.1024":                
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
