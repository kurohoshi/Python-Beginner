# def function
def function2():
  print('inside function2')

def function1():
  def function3(): # nested def function
    print('inside function3')

  print('inside function1')
  function2()
  print('still inside function1')
  function3()


print('outside function1')
function1()


# functions with argument(s)
# function2 is redefined, so latter def function2 is used
def function2(x):
  return 5*x

print(function2(4))

y = function2(7)
print(y)

# function with annotations, functionally irrelavent but helpful for validating return/parameter datetyping
def function4(x: int) -> int:
  return x

# lambda functions (aka anonymous functions) - mainly used for single line simple functions
lam1 = lambda x: x*2
print(lam1(4))

# returning a formatted string
lam2 = lambda x, y, z: f'{x} - {y} - {z}'
print(lam2('x', 'y', 'z'))

# IIFE
print( (lambda: 'This is a lambda function in a closure!')() )

# downsides of lambda functions: no traceback, making debugging a pain
