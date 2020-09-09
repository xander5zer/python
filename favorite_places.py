favorite_places = {
	'joi': ['toronto', 'niagara falls'],
	'neo': ['matrix', 'zeon'],
	'simba': ['lake', 'jungle'],
}

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places is:")
	for place in places:
		print(f"\t{place.title()}")