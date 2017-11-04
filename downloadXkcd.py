#! python3
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

url = 'https://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in local file xkcd -- exists_ok=True prevents program from throwing an exception if file already exits
while not url.endswith('#'): # very first comic ends with #
    # Download the page.
    print('Downloading page {}...'.format(url))
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicURL = 'https:' + comicElem[0].get('src')

            # Download the image.
            print('Downloading image {}...'.format(comicURL))
            res = requests.get(comicURL) # stores comic image in res
            try:
                res.raise_for_status()
            except Exception as exc:
                print('There was a problem: {}'.format(exc))
        except requests.exceptions.MissingSchema: # some comics have special content that's not an img, so skip those
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
