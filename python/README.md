# Python Web Scraper

The purpose of this project was to help me learn the basics of web scraping and practice in a relatively forgiving language.

## The Project

This project scrapes (roughly) two-week weather forecast data from two sources and displays the results of the operations performed on them.

### Information

Since different websites have different structures, it became necessary to either separate the scraping logic into different functions or different classes; I chose the latter. Each website class has a `.scrape(url)` method which handles the scraping logic. These classes are managed by a more general `WebScraper` class, which handles initially parsing the website, then chooses which website scraper class is used to extract the data.

These classes use a composition model rather than inheritance, due to the way the data is passed between them. This was probably influenced by my preference for FOOP whenever possible (OOP for organization, FP for logic). Alternatively, I could have implemented an abstract method using ABC. I actually tried that at first, but this ended up being both easier and faster for me (it also just felt more natural in this language; perhaps I just need more practice with them).

### Usage

1) Initialize a `WebScraper()` object.
2) Call its `.scrape(url)` method on either of the provided URLs.

The returned list will contain the low temperatures for the following (roughly) two weeks, which can then be used to perform various operations.

**Note: Because each website needs a custom scraper class implementation, only the two provided URLs are compatible. This may or may not change in the future.**

### What I learned

At the start of this project, I was unaware of the protections in place for web content, as I had never attempted to query them programmatically before. Some websites seem to simply have a disclaimer in the comments of the HTML, while others will return a custom message to the request, indicating that you don't have the appropriate permissions to use that content. Regardless of the method, no restricted content was used (that I am aware of; to be fair, I am still a little new at this. Apologies if I missed anything).

I did not realize this would be so common, so my original plan was to use several websites to gather my data; however, I ended up only finding two that allow their data to be used.

I would have used websites which have a dedicated API for interacting with their content, but as this is a web scraping project, I wanted to focus on parsing the HTML myself. That said, since I was only able to find two working websites, I may come back and add API functionality at some point.