from bs4 import BeautifulSoup
import requests

results = requests.get('https://www.whitehouse.gov/briefings-statements/')
print(results.status_code)
src = results.content
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('article')
print(*(link for link in links), sep='\n')


# for link in links:
#     if 'About' in link.text:
#         print(link)
#         print(link.attrs['href'])


if __name__ == '__main__':
    pass
