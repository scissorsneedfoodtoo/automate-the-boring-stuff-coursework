#! usr/bin/python3
# This program scans the script.txt file, and prompts the user for input
# whenever ADJECTIVE, NOUN, ADVERB, or VERB appears. After going through the
# entire file, a final-script.txt file is written with the user's inputs.

import re, string

# Open file, save content, and save to content
base_file = open('script.txt', 'r')
content = base_file.read()
base_file.close()

output = ""

# split content of script into a list or words and punctuation and loop over the contents
for item in re.findall("[\w']+|[.,!?;]", content):
    if item == 'ADJECTIVE':
        output += input('Enter an adjective: ') + ' '
    elif item == 'NOUN':
        output += input('Enter a noun: ') + ' '
    elif item == 'VERB':
        output += input('Enter a verb: ') + ' '
    else:
        if item in string.punctuation: # check if the current item is punctuation
            output = output.rstrip() # remove the whitespace off the end of the output string
            output += item + ' '
        else: # the current item is a word
            output += item + ' '

output += '\n'

final_file = open('final-script.txt', 'w')
final_file.write(output)
final_file.close()

print(output)
