#Working with Lists, Tuples, and Dictionaries

myString = 'This is my String.'
print(myString)
print(type(myString))
print(myString + ' is of the data type ' + str(type(myString)))

firstString = 'water'
secondString = 'fall'
thirdString = firstString + secondString
print(thirdString)


name = input('What is your name? ')
print(name)

color = input('What is your favourite colour? ')
animal = input('What is your favourite animal? ')

print('{}, you like a {} {}!'.format(name,color,animal))
