class Website1Scraper:
    def __init__(self, scraper):
        self.scraper = scraper

    def scrape(self, url):
        soup = self.scraper.parse_website(url)
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
