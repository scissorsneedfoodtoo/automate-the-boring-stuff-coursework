import bs4, requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?ie=UTF8&qid=1509449196&sr=8-1&keywords=automate+the+boring')
print('The price is {}.'.format(price))
