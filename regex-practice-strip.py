import re

def strip(str, to_strip=None):
    whitespace_regex = re.compile(r'^\s*(.*?)\s*$') # strips all whitespace
    if to_strip is None:
        return whitespace_regex.findall(str)[0] # return str group after stripping whitespace
    else:
        target = whitespace_regex.findall(str)[0] # strip whitespace and find remaining str
        char_regex = re.compile(r'[^' + to_strip + ']') # apply new regex to take out chars provided as argument --> provided as str to prevent literal interpretation of to_strip
        output = ''.join(char_regex.findall(target)) # join the resulting list and return
        return output

print(strip('   hello   ', 'test'))
print(strip('   speaking speaking loud and clear   ', 'ea'))
