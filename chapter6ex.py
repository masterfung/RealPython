#6.1 Exercises
desserts = ['ice cream', 'cookies']
desserts.sort()
print desserts
print desserts.index('ice cream')
food = desserts[:]
food.append('broccoli')
food.append('turnips')
print food
print desserts
print food[0:2]

breakfast = 'cookies, cookies, cookies'
breakfastBrokendown = breakfast.split(', ')
print breakfastBrokendown

#6.2 Exercises
cardinal_nums = ('first','second','third')
print cardinal_nums[1]
pos1, pos2, pos3 = cardinal_nums #tulip unpacking
print pos1, pos2, pos3

#6.3 Exercises
birthdays = {}

birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41' 

if not 'Yoda' in birthdays:
	birthdays['Yoda'] = 'unknown'
if not 'Darth Vader' in birthdays:
	birthdays['Darth Vader'] = 'unknown'

for name in birthdays:
	print name, birthdays[name]

del(birthdays['Darth Vader'])