user_names = []
if user_names:
	for user_name in user_names:
		if user_name == 'admin':
			print("Hellow admin, would you like to see a status report?")
		else:
			print(f"Hello {user_name}, thank you for logging in againe.")
else:
	print("We need to ind some users!")