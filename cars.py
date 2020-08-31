# cars = ['Porsche 911', 'Ferrari F50', 'BMW Z8']
# message = f"I want buy car {cars[0]}"

# print(message)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# cars.reverse()
# print(cars)

cars = ['audi', 'bmw', 'toyota', 'subaru']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
