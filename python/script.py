from scraper import WebScraper

"""
Idea:
Scrape weather data from various sources and display them in a single area,
along with combination info (average, median, etc.)
"""
scraper = WebScraper()

url1 = scraper.urls[0]
url2 = scraper.urls[1]

temps1 = scraper.scrape(url1)
temps2 = scraper.scrape(url2)

average1 = round(sum(temps1) / len(temps1), 2)
average2 = round(sum(temps2) / len(temps2), 2)
print(f"Average temperature from website 1: {average1}˚F")
print(f"Average temperature from website 2: {average2}˚F")
