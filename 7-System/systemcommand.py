# execute system commands from python

from sys import platform
import os

if platform == 'linux' or platform == 'linux2':
  os.system('cwd')
elif platform == 'win32' or platform == 'cygwin':
  os.system('cd')
else:
  print('unsupported OS!')
