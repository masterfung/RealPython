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