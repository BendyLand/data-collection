import requests
from bs4 import BeautifulSoup

""" 
Guide:
https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping

Website with sample data to practice scraping:
https://realpython.github.io/fake-jobs/ 

"""

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# print(page.text)
# print(soup.prettify())

