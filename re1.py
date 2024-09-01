import requests
from bs4 import BeautifulSoup

def parse(url):
    base_url = url
    all_html = []
    while True:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        all_html.append(soup)

        next_button = soup.find('a', {'data-auto-id': 'plp-pagination-next'})
        if next_button:
            url = base_url + next_button.get('href')
        else:
            break

    return all_html

all_html = parse('https://en.wikipedia.org/wiki/2024_Summer_Paralympics')

for item in all_html:
    div = item.find('div')
    print(div)
    # print('============')
    # if div:
    #     print(div.prettify()) 
    # else:
    #     print("No div found")


