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
            return Website1Scraper().scrape(url)
        elif url == self.urls[1]:
            return Website2Scraper().scrape(url)
        else:
            print("Invalid URL")


class Website2Scraper:
    def scrape(self, url):
        try:
            soup = WebScraper().parse_website(url)
            # gets the table of values
            forecast = soup.find(attrs={"id": "elbat"})
            # splits it into sub-tables for individual days
            tables = list(map(str, forecast.find_all("table")))
            temps = []
            for table in tables:
                content_lines = sorted(table.split("\n"), key=len)[-2]
                # the pattern that the temperatures are stored in looks like:
                # Lo: <span class="lan C">-3°C</span><span class="lan F">26°F
                result = re.search("Lo:.*?(\d+°F)", content_lines)
                # result[1] retrieves the captured value from the regex.
                # (values are captured in parenthesis, retrieved in order i.e. '1')
                temps.append(result[1][:-2])  # [:-2] removes ˚F
            # [1:] removes the current day's element, which Website1 doesn't include
            return list(map(int, temps))[1:]
        except:
            print("Unable to extract data from Website 2.")


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
                        temps.append(span.text[:-1])
            return list(map(int, temps))[
                :-2
            ]  # removes extra days that aren't included from other websites
        except:
            print("Unable to extract data from Website 1.")


scraper = WebScraper()

url1 = scraper.urls[0]
url2 = scraper.urls[1]

temps1 = scraper.scrape(url1)
temps2 = scraper.scrape(url2)

average1 = round(sum(temps1) / len(temps1), 2)
average2 = round(sum(temps2) / len(temps2), 2)
print(f"Average temperature from website 1: {average1}˚F")
print(f"Average temperature from website 2: {average2}˚F")
