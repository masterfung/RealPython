from __future__ import division

#4.1 Exercises
print 15 / 2.54

#4.2 Exercises
def cube(num):
	return num ** 3
	
print cube(5)
print cube(10)
print cube(2)

def multiply(a,b):
	result = a * b
	return result
print multiply(2,5)

#Run this result and you will find amazement on this concept
#this has to run a,b,c,d for each number before moving on. 
for n in xrange(1,4):
	for j in ('a','b','c', 'd'):
		print 'n =', n, 'and j =', j

#4.3 Exercises
for n in range(2,11):
	print n, '\n'
print 'The loop has finished! Thanks!'

count = 2
while (count < 11):
	print count+1, '\n'
	count += 1

def doubles(num):
    ''' Return the result of multiplying an input number by 2 '''
    return num * 2

# Call doubles to double the number 2 three times
myNum = input('Please enter a number: ')
for i in range(0,3):
    myNum = doubles(int(myNum))
    print(myNum)