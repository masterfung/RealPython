from __future__ import division

def invest(amount, rate, time):
	print 'Principal amount: {}'.format(amount)
	print 'Annual rate of return: {}'.format(rate)
	for x in xrange(1, time+1):
		amount = amount * (1 + rate)
		print 'Year {}: ${}'.format(x, amount)
	print '\n'

amount = raw_input('Enter an amount to invest: ')
rate = raw_input('What is the interest rate: ')
time = raw_input('Enter the total years of savings: ')
invest(int(amount), float(rate), int(time))
invest(100, 0.05, 8)
invest(2000, 0.025, 5)
invest(30000, 0.084, 5)