#Working with Lists
numbers = [3, 6, 2, 5, 8, 7, 12, 28]

max = numbers[0]
for number in numbers:
    if number > max:
        max = numbers
print(max)
print(numbers.count(5))
print(9 in numbers)

numbers.sort()
numbers.reverse()
numbers.clear()
numbers2 = numbers.copy()
numbers.append()

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        print(uniques)