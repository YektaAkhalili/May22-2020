toppings = ['pepperoni', 'cheese', 'pineapple','ranch','chicken','mushroom']

print("The first three items in the list are: ", toppings[:3])
print("The iterms from the middle of the list are: ", toppings[2:5])
print("The last three itms in the list are: ", toppings[-3:])

toppings.append("barbeque")
friendsPizza = toppings[:]
friendsPizza.append("vegtables")

print("My favorite pizzas are: ")
for topping in toppings:
	print(topping.title(), " pizza.\n")

print("My friend's favorite pizzas are: ")
for topping in friendsPizza:	
	print(topping.title(), " pizza.\n")
