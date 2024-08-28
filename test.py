import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.linkedin.com/search/results/companies/?keywords=bangladesh&origin=CLUSTER_EXPANSION&sid=dzj')
soup =  BeautifulSoup(r.content, 'html.parser')
 
s = soup.find('ul', class_ = 'reusable-search__entity-result-list list-style-none')
content = s.find_all('li')
print(content)


