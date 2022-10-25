# Creating a list called toppings that holds toppings.
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Creating a list called prices that holds the price.
prices = [2, 6, 1, 3, 2, 7, 2]

# Creating variable to list $2 pizza.
num_two_dollar_slices = prices.count(2)
# Print num_two_dollar_slices
print("We have", num_two_dollar_slices, "$2 pizzas")
# Printing empty line.
print("")

# Creating variables to calculate the length of the toppings.
num_pizzas = len(toppings)

# Printing string
print("We sell" ,num_pizzas,"different kinds of pizza!")
# Printing empty line.
print("")

# Creating two-dimensional list.
pizza_and_prices = [[prices[0], toppings[0]], [prices[1], toppings[1]], [prices[2], toppings[2]], [prices[3], toppings[3]], [prices[4], toppings[4]], [prices[5], toppings[5]], [prices[6], toppings[6]]]
# Print pizza_and_prices.
print(pizza_and_prices)
# Printing empty line.
print("")

# Sorting pizza_and_prices
pizza_and_prices.sort()
# Printing the sorted list
print(pizza_and_prices)
# Printing empty line.
print("")

# Creating a variable to store the cheapest pizza.
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
# Printing empty line.
print("")

# Creating a variable to store the priciest pizza.
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# Printing empty line.
print("")

# Removing anchovies as it is out of stock.
pizza_and_prices.pop()

# Adding new toppings with prices.
pizza_and_prices.insert(4, [2.5, "peppers"])
# Printing new list
print(pizza_and_prices)
# Printing empty line.
print("")

# Slicing the list and storing the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizza_and_prices[0:3]
# Printing the three cheapest pizza
print(three_cheapest)