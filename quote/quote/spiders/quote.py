import scrapy

URL = "http://quotes.toscrape.com/page/{page}/"

class QuotesSpider(scrapy.Spider):
    name = "quote"
    start_urls = [URL.format(page=page) for page in range(1,6)]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }