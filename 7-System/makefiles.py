# https://learn.microsoft.com/en-us/windows/python/scripting
# https://stackoverflow.com/questions/1274405/how-to-create-new-folder

import os
os.chdir('7-System')

foodlist = ['salad', 'pizza', 'pasta', 'casserol', 'cake', 'cookie', 'perogi', ]

# make dir if not exists
if not os.path.isdir('food'):
  os.makedirs('food')
fooddir = os.path.join('.', 'food')

# make files if not exists
for name in foodlist:
  if not os.path.isfile(name):
    with open(os.path.join(fooddir, name), 'w') as file:
      pass
