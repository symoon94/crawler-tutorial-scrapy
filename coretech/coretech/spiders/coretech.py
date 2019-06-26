import scrapy

URL = "https://coretech21c.co.kr/business/{navi}.jsp"
navilist = ["catalyst", "environment", "gas"]

class CoretechSpider(scrapy.Spider):
    name = "coretech"
    start_urls = [URL.format(navi=navi) for navi in navilist]

    def parse(self, response):
        for item in response.css('div.catalyst_pop'):
            yield {
                'name': item.css('p::text').get(),
            }
            for category in item.css('li'):
                yield {
                    category.css('p::text').get() : category.css("span::text").getall()
                }