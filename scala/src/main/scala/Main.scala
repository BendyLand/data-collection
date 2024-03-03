/* 
Idea:
Build a web scraper that uses an api to gather some form of data,
then scrape various sources to find articles which discuss the claims
*/

import bland.scraper.*

@main def run() = 
    val url = "https://weather.com/weather/tenday/l/Salem+CT?canonicalCityId=d6b4f8cb5f0e1db1761b2933184fd1de0779ec1fb8e9352bba2f7526d0000677"
    val scraper = Scraper
    val result = scraper.parseWebsite(url)
    println(result)
