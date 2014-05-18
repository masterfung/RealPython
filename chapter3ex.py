#3.1 Exercises

simpleValue = int('50')
print simpleValue * 10

anotherValue = float('20.3')
print anotherValue

greataddition = '2' + str(22)
print greataddition

#3.2 Exercies

weight = float('0.2')
animal = 'newt'
print str(weight) + " kg is the weight of the " + animal + "."
print '{} kg is the weight of the {}.'.format(weight, animal)
print '{1} kg is the weight of the {0}.'.format(animal, weight)
print '{weight} kg is the weight of the {animal}.'.format(weight = 0.2, animal = 'newt')

#3.3 Exercies
find1 = "AAA".find('a')
print find1

find2 = 'version 2.0'
resultFind2 = find2.find('2.0')
print str(resultFind2)

userPrompt = raw_input('Please enter a phrase and I will search!').find('e')
print str(userPrompt) + " is the first position of the letter e"

