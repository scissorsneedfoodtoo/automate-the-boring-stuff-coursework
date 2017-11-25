import os
import shutil

for folderName, subfolders, filenames in os.walk('/home/kris/exercism'): # returns 3 values in for loop, folder names, subfolder names, and file names
    # print('The folder is: {}'.format(folderName))
    # print('The subfolders in {} are: {}'.format(folderName, subfolders))
    # print('The filenames in {} are: {}'.format(folderName, filenames))
    # print()

    # for subfolder in subfolders:
    #     if 'fish' in subfolder:
    #         os.rmdir(subfolder)

    # for file in filenames: # file just returns string, not any sort of path
    #     if file.endswith('.py'):
    #         shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup'))

    # for file in filenames:
    #     if file.endswith('.backup'):
    #         os.unlink(os.path.join(folderName, file))
