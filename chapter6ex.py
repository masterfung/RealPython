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