from __future__ import division
from random import randint
#5.3 Exercises

userInput = raw_input('Please enter a word phrase or whatever your heart desires: ')
if len(userInput) < 5:
	print 'Your length is less than 5 characters long.'
elif len(userInput) > 5:
	print 'Your length is greater than 5 characters long'
else:
	print 'Your length is equal to five characters long!'

#5.4 Exercises
while True:
	myInput = raw_input('Please enter q or Q to quit: ')
	if (myInput == 'q') or (myInput == 'Q'):
		break


for i in range(1, 51):
	if i % 3 == 0:
		continue
	else:
		print i


#5.5 Exercises
while True:
	try:
		num = int(raw_input('Enter an integer: '))
		print num
		break
	except ValueError:
		print 'That was not an integer'


#5.6 Exercises
heads = 0
tails = 0
for trails in range(0, 10000):
	while randint(0,1) == 0:
		heads += 1
	else:
		tails += 1
	print heads / tails

print randint(1,6)


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for roll in range(0, 10000):
	while True:
		if randint(1,6) == 1:
			one += 1
			break
		elif randint(1,6) == 2:
			two += 1
			break
		elif randint(1,6) == 3:
			three +=1
			break
		elif randint(1,6) == 4:
			four +=1
			break
		elif randint(1,6) == 5:
			five +=1
			break
		elif randint(1,6) == 6:
			six +=1
			break
print 'The appearance of 1 is:', one, \
	'\nThe appearance of 2 is:', two, \
	'\nThe appearance of 3 is:', three, \
	'\nThe appearance of 4 is:', four, \
	'\nThe appearance of 5 is:', five, \
	'\nThe appearance of 6 is:', six, \
	'\nThe sum of all the appearance are:', one \
	+ two + three + four + five + six

