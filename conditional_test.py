# conditional 1
print("\nconditional 1")
my_string = '1string'
print("my_string == 1string")
print(my_string == '1string')

print("\nmy_string == 2string")
print(my_string == '2string')

# conditional 2
print("\nconditional 2")
user_name = 'Carolina'
print('conditional = lower')
print(user_name.lower() == 'carolina')
print('\nconditional = not lower')
print(user_name.lower() == 'Carolina')


# conditional 3
print("\nconditional 3")
age_0 = 20
age_1 = 21
print(f"age == 20:\n{age_0 == 20}")
print(f"age != 20:\n{age_0 != 20}")
print(f"age > 20:\n{age_0 > 20}")
print(f"age < 20:\n{age_0 < 20}")
print(f"age >= 20:\n{age_0 >= 20}")
print(f"age <= 20:\n{age_0 <= 20}")

# conditional 4
print("\nconditional 4")
print(f"conditional AND True:\n{age_0 == 20 and age_1 == 21}")
print(f"conditional AND False:\n{age_0 == 21 and age_1 == 21}")
print(f"conditional OR True:\n{age_0 == 20 or age_1 == 21}")
print(f"conditional OR False:\n{age_0 == 21 or age_1 == 22}")

# conditional 5
print("\nconditional 5")
user_list = ['user0', 'user1', 'user2', 'user3',]
print('user1' in user_list)

# conditional 6
print("\nconditional 6")
print('user7' in user_list)