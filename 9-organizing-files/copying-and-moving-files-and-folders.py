import shutil

# shutil.copy('/home/kris/spam.txt', '/home/kris/Documents')
#
# shutil.copy('/home/kris/spam.txt', '/home/kris/Documents/delicious/spamspamspam.txt') # can rename file here
#
# shutil.copytree('/home/kris/Documents/delicious', '/home/kris/Documents/delicious-backups')

shutil.move('/home/kris/spam.txt', '/home/kris/spamspam.txt') # no rename, just moving, like with command line linux
