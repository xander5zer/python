favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'adward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

# 6. Словари


	

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

# names = ['jen', 'sarah', 'adward', 'david', 'kurt', 'edgard']

# for name in names:
# 	if name in favorite_languages.keys():
# 		print(f"{name.title()}, thank you for taking the poll.")
# 	else:
# 		print(f"{name.title()}, please take our poll!")
