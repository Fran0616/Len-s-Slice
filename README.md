# Len-s-Slice
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

Taks
=

1. To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:
- "pepperoni" 
- "pineapple"
- "cheese"
- "sausage"
- "olives"
- "anchovies"
- "mushrooms"

2. To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
- 2
- 6
- 1
- 3
- 2
- 7
- 2

3. Your boss wants you to do some research on $2 slices.Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
4. Find the length of the toppings list and store it in a variable called num_pizzas.
5. Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
6. Convert our toppings and prices lists into a two-dimensional list called pizza_and_prices that has the following associated values. Each sublist in pizza_and_prices should have one pizza topping and an associated price
7. Print pizza_and_prices.
8. Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
9. Store the first element of pizza_and_prices in a variable called cheapest_pizza.
10. A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!” Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
11. It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
12. Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Add the new peppers pizza topping to our list pizza_and_prices. Note: Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!
13. Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
14. Great job! The mice are very pleased and will be leaving you a 5-star review. Print the three_cheapest list.

[Scripy.py](https://github.com/Fran0616/Len-s-Slice/blob/main/LenSlice.py)
=
```
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
```
Output
=
```
We sell  7 different kinds of pizza!
[[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
[[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]
[[1, 'cheese'], [2, 'mushrooms'], [2, 'olives']]
```
Conclusion 
= 
List allows for easy use of data in python. The value of a list is store inside a bracket separated by commas. The values in a list do not need to be unique, and you can create an empty list. In order to complete this project I had to used several of the build in python module, and function. I used the len function to determine the number of item that was in the num_pizza list. Then I created a 2D list call pizza_and_prices. A 2D list is a list that contain other list. In this project I created a 2D list to store the prices with its associated topping. The 8th taks required the prices_and_pizza list to be ordered by increasing prices. The sort method sort content in a list. It modifies the original list, and has no value. To modify elemet in a list simply need to create a new variable to access the list with its index. The pop method is use to remove an item from a listand instert method to add items to a list.The insert method takes two inputs, the index you want to insert into, and the elemnet you want to insert at the specefic index.
