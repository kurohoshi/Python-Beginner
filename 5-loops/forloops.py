# iterating through a list
for item in [1, 2]:
  print(item)

# iterating through a list variable
x = [1, 2, 3]
for item in x:
  print(item)

# totalling a list of numbers
total1 = 0
for item in x:
  total1 += item
print(total1)

# using range to iterate thru a sequence of numbers
total2 = 0
for num in range(1,6):
  print(num)
  total2 += num
print(total2)

# multiples of a and b that are less than 100
a = 6
b = 7
tally = 0
for num in range(1, 100):
  if not (num % a and num % b):
    tally += 1
print(f'number of multiples: {tally}')
