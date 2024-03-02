from scraper import WebScraper
from statistics import mean, median, mode

scraper = WebScraper()

url1 = scraper.urls[0]
url2 = scraper.urls[1]

temps1 = scraper.scrape(url1)
temps2 = scraper.scrape(url2)

average1 = round(mean(temps1), 2)
average2 = round(mean(temps2), 2)
print(f"\nAverage temperature from website 1: {average1}˚F")
print(f"Average temperature from website 2: {average2}˚F\n")

median1 = median(temps1)
median2 = median(temps2)
print(f"Median temperature from website 1: {median1}˚F")
print(f"Median temperature from website 2: {median2}˚F\n")

mode1 = mode(temps1)
mode2 = mode(temps2)
print(f"Mode from website 1: {mode1}")
print(f"Mode from website 2: {mode2}\n")
