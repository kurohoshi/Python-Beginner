# https://wiki.python.org/moin/Generators
# https://realpython.com/introduction-to-python-generators/

# basic generator function
def listfeed(x):
  num = 0
  while num < x:
    yield num
    num += 1

# iterate through generated values
for gennum in listfeed(8):
  print(gennum)

# can manually advance to the next value of the generator
# Handle StopIteration exception with a try/except
gen = listfeed(3)

try:
  print(next(gen))
  print(next(gen))
  print(next(gen))
  print(next(gen))
except StopIteration:
  print('Reached end of generator values!')


# using .send() to send stuff back to the generator, which in turn advances to the next yield value
# .send() cannot be executed on the 0th iteration generator
def genexample2(x):
  num = 0
  while num < x:
    i = (yield num)
    print(i)
    num += 1

y = genexample2(10)
try:
  print(next(y))
  print(y.send(10000))
  print(y.send(10000))
except StopIteration:
  print('Reached end of generator values!')