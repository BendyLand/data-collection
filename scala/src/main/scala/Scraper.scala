package bland.scraper

import org.jsoup.*
import org.jsoup.nodes.Document
import scala.jdk.CollectionConverters.*

object Scraper:
    def parseWebsite(url: String): Document = 
        Jsoup.connect(url).get()