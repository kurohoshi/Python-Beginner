# class methods all need 'self' argument
class Robot:
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight

  def introduce_self(self):
    print(f'Hi! My name is {self.name}.')

  
r1 = Robot('Bob', 'red', 23)
r1.introduce_self()



class Person:
  def __init__(self, name, personality, isSitting, robotOwn):
    self.name = name
    self.personality = personality
    self.isSitting = isSitting
    self.robotOwn = robotOwn

  def sit_down(self):
    self.isSitting = True

  def stand_up(self):
    self.isSitting = False

p1 = Person('Dave', 'loud', True, r1)

p1.robotOwn.introduce_self()
