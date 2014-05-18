cel = raw_input('Please enter a temp to convert into F: ')
def celsius(cel):
	conversiontoF = int(cel) * 9/5 + 32
	return conversiontoF
print cel, 'degrees C =', celsius(cel), 'degrees F'

fah = raw_input('Please enter a temp to convert into C: ')
def fahrenheit(fah):
	conversiontoC = (int(fah) - 32) * 5/9
	return conversiontoC
print fah, 'degrees F =', fahrenheit(fah), 'degrees C'