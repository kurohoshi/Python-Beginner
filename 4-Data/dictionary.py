# keys can be either strings or numbers

d = {}
d = dict()
d = {'new': 1, 'dict': 2}

print(d['new'])

# add new key-value pair
d['newkey'] = 50

print(d)

# iterating through a dictionary
for key, value in d.items():
  print(f'{key}: {value}')
  