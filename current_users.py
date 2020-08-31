current_users = ['User1', 'USER2', 'user3', 'user4']
current_users_base = []
for user_name in current_users:
	current_users_base.append(user_name.lower())

new_users = ['UsEr1', 'useR2', 'user5', 'user6', 'user7']
new_users_lower = []
for new_user in new_users:
	new_users_lower.append(new_user.lower())

for new_user in new_users_lower:
	if new_user in current_users_base:
		print("This name is taken, please enter another name")
	else:
		print(f"Welcome {new_user}")