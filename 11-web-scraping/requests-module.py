import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.status_code) # should print 200 for all good

print(len(res.text))

print(res.text[:500])

res.raise_for_status() # raises exception if there is a problem downloading the file and does nothing if it succeeds

playFile = open('RomeoAndJuliet.txt', 'wb') # must be writted with write-binary to maintain the unicode encoding of the text
for chunk in res.iter_content(100000): # iter_content returns chunks of the content on each iteration through the loop. Each chunk is of the bytes data type, and you can specify how many bytes each chunk will contain
    playFile.write(chunk)

playFile.close()
