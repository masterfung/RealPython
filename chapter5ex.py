#5.3 Exercises

userInput = raw_input('Please enter a word phrase or whatever your heart desires: ')
if len(userInput) < 5:
	print 'Your length is less than 5 characters long.'
elif len(userInput) > 5:
	print 'Your length is greater than 5 characters long'
else:
	print 'Your length is equal to five characters long!'
