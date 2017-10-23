import re

# namesRegex = re.compile(r'Agent \w+')

# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

# print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))




# namesRegex = re.compile(r'Agent (\w)\w*') # want to capture first letter of word following agent in own group, followed by 0 or more letter characters

# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # ['A', 'B']

# print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

print(phoneRegex.findall('999-123-2309'))
