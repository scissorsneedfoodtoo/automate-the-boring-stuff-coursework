import re
#
# batRegex = re.compile(r'Bat(wo)?man') # same as (r'Batman|Batwoman')
# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())

# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
# mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.') # produces error--no area code
# print(mo.group())

# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # makes area code optional--can appear once or zero times
# mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
# print(mo.group())

# batRegex = re.compile(r'Bat(wo)*man') # * means pattern can appear 0 or more times--any number of times
# mo = batRegex.search('The Adventures of Batwowowowoman')
# print(mo.group())

# batRegex = re.compile(r'Bat(wo)+man') # + means pattern must appear one or more times
# # mo = batRegex.search('The Adventures of Batman') # error due to wo not appearing
# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())

# regex = re.compile(r'\+\*\?')
# print(regex.search('I learned about +*? regex syntax').group())

# regex = re.compile(r'(\+\*\?)+')
# print(regex.search('I learned about +*?+*?+*?+*?+*?+*? regex syntax').group())

# haRegex = re.compile(r'(Ha){3}')
# print(haRegex.search('He said "HaHaHa"').group())

# phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
# print(phoneRegex.search('My numbers are 415-555-1234, 555-4242, 212-555-0000').group())

# haRegex = re.compile(r'(Ha){3,5}') # {x, y} -- between x and y repetitions, but works like slices where you can leave off values,
# # like {,5}--or 0 to 5--or {3,}--unbounded, 3, to however many
# print(haRegex.search('He said "HaHaHaHaHa"').group())

# digitRegex = re.compile(r'(\d){3,5}')
# print(digitRegex.search('1234567890').group()) # returns 12345, or the first, greedy match (longest possible string that matches the pattern)

digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890').group()) # returns 123, or the non greedy match, or the smallest possible string
