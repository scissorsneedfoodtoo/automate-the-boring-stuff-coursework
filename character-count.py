import pprint

rj_file = open('rj.txt', 'r')
count = {}
for char in rj_file.read().upper():
    count.setdefault(char, 0)
    count[char] += 1

# print(rj_file.read())
output = pprint.pformat(count)
print(output)

rj_file.close()
