favorite_numbers = {
	'david': ['45'],
	'lopes': ['10'],
	'howard': ['17'],
	'stiv': ['20'],
	'malcolm': ['55'],
}

for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers is:")
	for number in numbers:
		print(f"\t{number}")


# print(f"David favorite number is {favorite_numbers['david']}")
# print(f"Lopes favorite number is {favorite_numbers['lopes']}")
# print(f"Howard favorite number is {favorite_numbers['howard']}")
# print(f"Stiv favorite number is {favorite_numbers['stiv']}")
# print(f"Malcolm favorite number is {favorite_numbers['malcolm']}")