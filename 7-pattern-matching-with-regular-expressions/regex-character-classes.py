import re

# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# numbers = '555-555-1234, 123-456-8889' # video uses resume as example
#
# print(phoneRegex.findall(numbers)) # prints list of strings that match pattern

# phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # regex with 2 or more groups
# numbers = '555-555-1234, 123-456-8889'
#
# print(phoneRegex.findall(numbers)) # prints list of tuples, and each tuple has multiple string values

# lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
#
# xmasRegex = re.compile(r'\d+\s\w+') # 1 or more digits, a single space, followed by 1 or more word characters
# print(xmasRegex.findall(lyrics))

# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('Robocop eats baby food'))

# doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
# print(doubleVowelRegex.findall('Robocop eats baby food'))

consonantsRegex = re.compile(r'[^aeiouAEIOU]') # finds anything that's NOT a vowel, including spaces and punctuation
print(consonantsRegex.findall('Robocop eats baby food'))
