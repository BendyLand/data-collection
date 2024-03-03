package bland.scraper

import org.jsoup.*
import org.jsoup.nodes.Document
import scala.jdk.CollectionConverters.*

object Scraper:
    def scrape(url: String): Document = 
        Jsoup.connect(url).get()