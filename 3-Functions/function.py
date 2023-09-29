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
