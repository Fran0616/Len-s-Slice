topping = ["pepperoni","pineapple", "cheese","sausage", "olives", "anchovies", "mushrooms"]#list to keep track of the pizza topping
prices = [2,6,1,3,2,7,2]#list to store the price for each topping
num_two_dollar_slices = prices.count(2)#Count the number of occurrences of 2 in the prices list

num_pizzas = len(topping) #length of the toppings list
print("We sell ", num_pizzas, "different kinds of pizza!")
#price and topping 2d list
pizza_and_prices = [[prices[0],topping[0]],
[prices[1],topping[1]],
[prices[2],topping[2]],
[prices[3],topping[3]],
[prices[4],topping[4]],
[prices[5],topping[5]],
[prices[6],topping[6]],
]

print(pizza_and_prices)

#sorting and slicing
pizza_and_prices.sort()# sort price in increasing price
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]#cheapest pizza
priciest_pizza = pizza_and_prices[-1]#most expensve pizza
pizza_and_prices.pop()# remove the most expensive pizza 
pizza_and_prices.insert(4,[2.5, "peppers"])
three_cheapest = pizza_and_prices[0:3] #slice the first three elements
print(three_cheapest)
