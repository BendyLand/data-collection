import requests
from bs4 import BeautifulSoup
from website1 import Website1Scraper
from website2 import Website2Scraper

url_1 = "https://weather.com/weather/tenday/l/Salem+CT?canonicalCityId=d6b4f8cb5f0e1db1761b2933184fd1de0779ec1fb8e9352bba2f7526d0000677"
url_2 = "https://www.weatherwx.com/14dayweather/ct/east+windsor.html"


class WebScraper:
    def __init__(self):
        self.urls = [url_1, url_2]
        self.scraper1 = Website1Scraper(self)
        self.scraper2 = Website2Scraper(self)

    def parse_website(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def scrape(self, url):
        if url == self.urls[0]:
            return self.scraper1.scrape(url)
        elif url == self.urls[1]:
            return self.scraper2.scrape(url)
        elif url == self.urls[2]:
            return self.scraper3.scrape(url)
        else:
            print("Invalid URL")
