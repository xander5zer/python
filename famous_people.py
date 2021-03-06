people = {
	'dbeckham':{
		'first': 'david',
		'last': 'beckham',
		'age': '45',
		'location': 'London',
	},

	'aeinstein':{
		'first': 'albert',
		'last': 'aeinstain',
		'age': '76',
		'location': 'princeton'
	},
	
	'mcurie':{
		'first': 'marie',
		'last': 'curie',
		'age': '66',
		'location': 'paris',
	}
}

for username, user_info in people.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	age = user_info['age']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tAge: {age}")
	print(f"\tLocation: {location.title()}")
