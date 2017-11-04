#! /usr/bin/python3
#lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {}'.format(exc))

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result.
linkElems = soup.select('.r a') # Finds all <a> elements with the r CSS class (<h3 class="r"><a></a></h3>)
numOpen = min(5, len(linkElems)) # Use min in case the search has fewer than 5 results
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
    # print(linkElems[i].get('href'))
