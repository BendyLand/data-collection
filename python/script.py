import requests
import re
from bs4 import BeautifulSoup

"""
Idea:
Scrape weather data from various sources and display them in a single area,
along with combination info (average, median, etc.)
"""

url_1 = "https://weather.com/weather/tenday/l/Salem+CT?canonicalCityId=d6b4f8cb5f0e1db1761b2933184fd1de0779ec1fb8e9352bba2f7526d0000677"
url_2 = "https://www.weatherwx.com/14dayweather/ct/east+windsor.html"


class WebScraper:
    def __init__(self):
        self.urls = [url_1, url_2]

    def parse_website(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def scrape(self, url):
        if url == self.urls[0]:
            Website1Scraper().scrape(url)
        elif url == self.urls[1]:
            Website2Scraper().scrape(url)
        else:
            print("Invalid URL")


class Website2Scraper:
    def scrape(self, url):
        soup = WebScraper().parse_website(url)
        # gets the table of values
        forecast = soup.find(attrs={"id": "elbat"})
        tables = list(map(str, forecast.find_all("table")))
        
        
        


class Website1Scraper(WebScraper):
    def scrape(self, url):
        soup = WebScraper().parse_website(url)
        try:
            parent = soup.find(
                attrs={
                    "class": "Card--content--1GQMr DailyForecast--CardContent--2YlvT"
                }
            )
            spans = parent.find_all("span")
            temps = []
            for span in spans:
                if "lowTempValue" in str(span):
                    if span.text[0] != "/":
                        temps.append(int(span.text[:-1]))

            return temps
        except:
            print("Unable to extract temperatures")


scraper = WebScraper()
url1 = scraper.urls[0]
temps1 = scraper.scrape(url1)

url2 = scraper.urls[1]
scraper.scrape(url2)
