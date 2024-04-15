def calculate_chocolate_bars(total_money, price):  
    bars = total_money // price  
    change = total_money % price 
    return bars, change

# Example usage:  
total_money = 100  
price = 7  
bars, change = calculate_chocolate_bars(total_money, price)  
print(f"You can afford {bars} chocolate bars with {change} left over.")

total_money = int(input("please enter your total_money:"))
price = int(input("please enter the price:"))
bars, change = calculate_chocolate_bars(total_money, price)  
print(f"You can afford {bars} chocolate bars with {change} left over.")