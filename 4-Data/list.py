list = [3, 5, 'no']
print(list)

# append new items to list
list.append(7)
print(list)

# lists can have list items
list.append(['nested', 'list'])
print(list)

# pop off last item
list.pop()
print(list)

# direct access to a list item
print(list[3])

# direct modification to a list item
list[3] = 'newValue'
print(list)

# easy method to swap variables
list[0], list[2] = list[2], list[0]
print(list)

# list comprehension
listC1 = [4, 7, 3, 7, 2, 1]
listC2 = [x**2 for x in listC1]
print(listC2)

listSquared = [x**2 for x in range(1,7)]
print(listSquared)
