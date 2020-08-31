# pizza_names = ['papperoni', '4 cheeses', 'texas']
# # for pizza in pizza_names:
# # 	print(f"I like {pizza} pizza!")
# # print("\nI really love pizza!")\
# friend_pizzas = pizza_names[:]

# pizza_names.append('margaritta')
# friend_pizzas.append('salamy')

# print('My favorite pizzas are:')
# for pizza in pizza_names:
# 	print(pizza)

# print('\nMy friend’s favorite pizzas are:')
# for pizza in friend_pizzas:
# 	print(pizza)

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
	"with following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)