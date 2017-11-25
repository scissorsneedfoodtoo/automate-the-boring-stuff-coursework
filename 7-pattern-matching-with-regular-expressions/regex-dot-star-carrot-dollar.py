import re

# beginsWithHelloRegex = re.compile(r'^Hello') # string must start with Hello -- xHellojlsi doesn't count!
# print(beginsWithHelloRegex.search('Hello there!').group())
# # beginsWithHelloRegex.search('He said "Hello!""') === None

# endsWithWorldRegex = re.compile(r'world!$') # string must start with Hello -- xHellojlsi doesn't count!
# print(endsWithWorldRegex.search('Hello world!').group())
# # endsWithWorldRegex.search('Hello world!sdfsdf') === None

# allDigitsRegex = re.compile(r'^\d+$') # starts with all digits and ends with all digits
# print(allDigitsRegex.search('98209384987298324').group())
# # allDigitsRegex.search('982093849xxxx87298324') === None

# atRegex = re.compile(r'.{1,2}at') # anything followed by at
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # . means anything and * is 0 or more, so basically any pattern
# print(nameRegex.findall('First Name: Kris Last Name: Koishigawa'))

# serve = '<To serve humans> for dinner.>'
# # nongreedy = re.compile(r'<(.*?)>')
# # print(nongreedy.findall(serve)) # prints ['To serve humans']
# greedy = re.compile(r'<(.*)>')
# print(greedy.findall(serve)) # prints ['To serve humans> for dinner.']

# prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
# # dotStar = re.compile(r'.*')
# # print(dotStar.search(prime).group()) # Serve the public trust.
# dotStar = re.compile(r'.*', re.DOTALL)
# print(dotStar.search(prime).group()) # Serve the public trust.\nProtect the innocent.\nUphold the law.
#

# vowelRegex = re.compile(r'[aeiou]') # forgot to add AEIOU to character class
# print(vowelRegex.findall('Al, why is your programming book talk about RoboCop so much?')) # ['i', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']

ignoreVowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) # can also pass re.I
print(ignoreVowelRegex.findall('Al, why is your programming book talk about RoboCop so much?')) # ['A', 'i', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
