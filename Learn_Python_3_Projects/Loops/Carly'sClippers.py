# hairstyles variable to hold types of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# prices variable to hold the prices of hairstyles
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# last_week variable to hold the number of purchases of each hairstyle type in the last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# set total price to 0
total_price = 0

# print length of prices
print(len(prices))

# for loop to calculate total price
for price in prices:
  total_price = total_price + price

# average price variable & print average_price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# new_prices comprehension list to cut all the prices by 5 dollars & print new_prices
new_prices = [price - 5 for price in prices]
print(new_prices)

# set total_revenue variable to 0
total_revenue = 0

# for loop to create a variable i 
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# print total_revenue variable
print("Total Revenue: " + str(total_revenue))

# average_daily_revenue varaible to hold average daily revenue & print average_daily_revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))

# cuts_under_30 comprehension list to add all hairstyles under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

# print cuts_under_30
print("Products under $30: " + str(cuts_under_30))