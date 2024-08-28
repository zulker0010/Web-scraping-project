import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.linkedin.com/search/results/companies/?keywords=Bangladesh&origin=GLOBAL_SEARCH_HEADER&sid=.~o')
print(r)
print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())