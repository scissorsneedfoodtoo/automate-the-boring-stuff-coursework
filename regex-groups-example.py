import re

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print(mo.group(1)) # area code
# print(mo.group(2)) # rest of num

# phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
#
# mo = phoneNumRegex.search('My number is (415) 555-4242')
# print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
