import re


class Website2Scraper:
    def __init__(self, scraper):
        self.scraper = scraper

    def scrape(self, url):
        try:
            soup = self.scraper.parse_website(url)
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
