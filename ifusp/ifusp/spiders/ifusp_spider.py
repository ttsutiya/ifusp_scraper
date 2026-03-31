import scrapy


class IfuspSpider(scrapy.Spider):
    name = "ifusp"

    async def start(self):
        urls = ["https://portal.if.usp.br/carreiras/pt-br/oportunidades"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
