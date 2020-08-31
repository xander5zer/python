favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'adward': 'ruby',
	'phil': 'python',
}


# 1
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite languages is {language}.")

# 2
# for name, language in favorite_languages.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}.")

# 3 Перебор всех ключей в словаре
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
# 	print(name.title())

# 	if name in friends:
# 		language = favorite_languages[name].title()
# 		print(f"\t{name.title()}, I see you love {language}!")

# 4
# if 'erin' not in favorite_languages.keys():
# 	print("Erin, please take our poll!")

# 5 Перебор ключей словаря в определенном порядке
# for name in sorted(favorite_languages.keys()):
# 	print(f"{name.title()}, thank you for taking the poll.")

# 6 Перебор всех значений в словаре
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
# 	print(language.title())

# 6.6 Опрос

names = ['jen', 'sarah', 'adward', 'david', 'kurt', 'edgard', 'potap']

for name in favorite_languages.keys():
	print(f"{name.title()}, thank you for taking the poll.")

	if name in names:
		print(f"{name.title()}, please take our poll!")
