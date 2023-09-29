# https://learn.microsoft.com/en-us/windows/python/scripting
# https://stackoverflow.com/questions/1274405/how-to-create-new-folder

import datetime
import os
os.chdir('7-System')
fooddir = os.path.join('.', 'food')

# modify file names
for directory, subdir_list, file_list in os.walk(fooddir):
  for name in file_list:
    source_name = os.path.join(directory, name)
    timestamp = os.path.getmtime(source_name)
    modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')
    target_name = os.path.join(directory, f'{modified_date}_{name}')

    print(f'Renaming: {source_name} to: {target_name}')

    os.rename(source_name, target_name)
