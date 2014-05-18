def divisor(num):
	print 'Enter an integer: {}'.format(num)
	for i in range(1, num+1):
		if num % i == 0:
			print '{} is a divisor of {}'.format(i, num)
	print('\n')

userInput = raw_input("Enter a number please: ")
myNum = int(userInput)
divisor(myNum)