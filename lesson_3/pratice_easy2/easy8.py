# Determine whether the following dictionary of people and their age contains an entry for 'Spot':


ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print(ages.get('Spot' , 'Not here'))

print(32 in ages.values())