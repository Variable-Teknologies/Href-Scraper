from bs4 import BeautifulSoup as bs
import requests
from progress.counter import Counter
import json


# TODO: make a loading bar while it is scraping
# Can't determing length so must be numberless or only show amount scraped

# gets all hrefs from given url
def getHrefs(base, uri, hrefs):
    # creates the url to scrape from
    url = base + uri
    # gets html of url
    urlHtml = requests.get(url).content
    # soup object of html
    soup = bs(urlHtml, 'lxml')
    # goes through each tag with an href in the page
    for tag in soup.find_all(href=True):
        # href in tag
        href = tag['href']
        href
        # checks that it is uri and that it is not '/' or '#' and that it isn't already in list
        if (href.startswith('/') and not href.startswith('//') and len(href) > 1 and href not in hrefs):
            # adds href to list
            hrefs.append(href)

count = Counter("Scraping : ")
# list for hrefs
hrefs = []
# input for base url,
base = input()
# checks if base ends with '/'
if(base.endswith('/')):
    # postion of last character before '/'
    lastPos = len(base) - 1
    # removes '/' from base
    base = base[0:lastPos]
# gets all the hrefs from base URL
getHrefs(base, "", hrefs)
# loops through hrefs
# hrefs will be added as it loops through each href
# but will end once all hrefs have been check
for href in hrefs:
    # gets all hrefs from sub-url
    getHrefs(base, href, hrefs)
    count.next()
# dictionary for json format
dicti = {}
# adds hrefs to dictionary with base as the key
dicti[base] = hrefs
# writes it to json format
with open("website.json", 'w') as file:
    json.dump(dicti, file)
