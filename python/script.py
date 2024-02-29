import requests
from bs4 import BeautifulSoup

"""
Idea:
Scrape weather data from various sources and display them in a single area,
along with combination info (average, median, etc.)
"""

url_1 = "https://weather.com/weather/tenday/l/Salem+CT?canonicalCityId=d6b4f8cb5f0e1db1761b2933184fd1de0779ec1fb8e9352bba2f7526d0000677"


class WebScraper:
    def __init__(self):
        self.urls = [url_1]

    def scrape(self, url):
        match url:
            case url_1:
                Website1Scraper().scrape(url)


class Website1Scraper:
    def scrape(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
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
            print(
                "Average low temp for the next two weeks:", str(sum(temps) / len(temps))
            )
        except:
            print("Unable to extract temperatures")


scraper = WebScraper()
url = scraper.urls[0]
scraper.scrape(url=url)
