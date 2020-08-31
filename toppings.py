# old
# reguested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# if 'mushrooms' in reguested_topping:
# 	print("Adding mashrooms.")
# if 'papperoni' in reguested_topping:
# 	print("Adding papperoni.")
# if 'extra cheese' in reguested_topping:
# 	print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# Проверка специальных значений

# reguested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for reguested_topping in reguested_toppings:
# 	if reguested_topping == 'green peppers':
# 		print("Sorry, we are out of green peppers right now.")
# 	else:
# 		print(f"Adding {reguested_topping}.")

# print("\nFinished making your pizza!")

# Проверка наличия элементов в списке

# requested_toppings = []
# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		print(f"Adding {requested_topping}.")
# 	print("\nFinished making your pizza!")
# else:
# 	print("Are you sure you want a plain pizza?")

#  Множественные списки

available_toppings = ['mushrooms', 'olives', 'green pappers', 'papperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french rfies', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")