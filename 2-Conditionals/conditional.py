# true and false statements
if True:
  print('It\'s true!')

if False:
  print('It\'s true!')
else:
  print('It\'s false!')

# variable comparison
x = 5
y = 3

if x < y:
  print('x is less than y')
elif x == y:
  print('x is equal to y')
else:
  print('x is greater than y')

# indentation determines scope
if True:
  print('conditional print 1!')
  print('conditional print 2!')
else:
  print('did not print!')

# truthy/falsy values
if 0:
  print('0 is truthy!')
else:
  print('0 is falsy!')

if 1:
  print('1 is truthy!')
else:
  print('1 is falsy!')

# Falsy Values: [], (), {}, set(), "", range(0), 0, 0.0, 0j, None, False
# Truthy Values: anything that isn't a falsy value
