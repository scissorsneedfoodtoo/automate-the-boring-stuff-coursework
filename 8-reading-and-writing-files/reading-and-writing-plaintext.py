# helloFile = open('hello.txt') # read mode default
# content = helloFile.read()

# content = helloFile.readlines()

# helloFile = open('hello.txt', 'w') # open file in write mode
#
# helloFile.write("Hellooooo!\n")
# helloFile.write("Hellooooo!\n")
# helloFile.write("Hellooooo!\n")
#
# helloFile.close() # close file before program finishes

# baconFile = open('bacon.txt', 'w')
#
# baconFile.write('Bacon is not a vegetable.') # write to baconFile
#
# baconFile.close()

# baconFile = open('bacon.txt', 'a') # append to baconFile
#
# baconFile.write('\n\nBacon is delicious.')
#
# baconFile.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

shelfFile.close()
