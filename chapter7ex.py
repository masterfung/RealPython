#7.1 Exercises
with open('Practice Files/Chapter 7/Practice files/poem.txt', 'r') as myInput, open('Practice Files/Chapter 7/Practice files/test.txt', 'w') as myOutput:
	for line in myInput.readline():
		myOutput.write(line)