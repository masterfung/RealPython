import os

#7.1 Exercises
firstInput = open('Practice Files/Chapter 7/Practice files/poem.txt', 'r')
subject = firstInput.readline()
while subject != "":
	print subject,
	subject = firstInput.readline()
firstInput.close()

with open('Practice Files/Chapter 7/Practice files/poem.txt', 'r') as myInput, open('Practice Files/Chapter 7/Practice files/test.txt', 'w') as myOutput:
	for line in myInput.readline():
		myOutput.write(line)


somethingFun = open('Practice Files/Chapter 7/Practice files/test.txt', 'a')
somethingAmazing = ["I saw the newest X-Men movie on release night and I still love the X-Men! Go see it!"]
somethingFun.writelines(somethingAmazing)
somethingFun.close()

#7.2 Exercises