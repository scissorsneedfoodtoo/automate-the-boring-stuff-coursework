import os

# print(os.path.join('folder1', 'folder2', 'file.png'))

# print(os.getcwd()) # get current working directory

# os.chdir() # pass new directory path to change cwd

# print(os.path.abspath('table-printer.py')) # returns string of absolute path that is passed to it

# os.path.isabs() # returns true if passed an absolute path

# os.path.relpath('path1', 'path2') # gives relative path of two absolute paths

# print(os.path.basename('/Documents/automate-the-boring-stuff-with-python/filenames-absolute-relative-paths.py')) # pulls of the dir name and returns the basename of the file

# os.path.exists('path-name') # returns true if path exits

# print(os.path.getsize('Automate_the_Boring_Stuff_onlinematerials.zip')) # gets filesize in bytes

# print(os.listdir('/home/kris/Documents/automate-the-boring-stuff-with-python')) # returns list of files in path

totalSize = 0

for filename in os.listdir('/home/kris/Documents/automate-the-boring-stuff-with-python'):
    if not os.path.isfile(os.path.join('/home/kris/Documents/automate-the-boring-stuff-with-python', filename)):
        continue
    totalSize += os.path.getsize(os.path.join('/home/kris/Documents/automate-the-boring-stuff-with-python', filename))

print(totalSize)

# os.makedirs('delicious/walnut/waffles') # will make folders in specified relative or absolute directory
