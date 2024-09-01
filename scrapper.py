from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Main_Page'

page = requests.get(url)

soup =BeautifulSoup(page.text, 'html')

