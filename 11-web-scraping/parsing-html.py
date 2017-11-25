import bs4, requests

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?ie=UTF8&qid=1509449196&sr=8-1&keywords=automate+the+boring')

res.raise_for_status() # checks for errors

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')

print(elems[0].text.strip())
