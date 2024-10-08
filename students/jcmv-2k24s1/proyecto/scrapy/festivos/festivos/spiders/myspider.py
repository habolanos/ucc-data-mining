import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["www.festivos.com.co"]
    start_urls = ["https://www.festivos.com.co/historico"]

    def parse(self, response):
        rows = response.css('#myTable tbody tr')
        for row in rows:
            yield {
                'Año': row.css('td:nth-child(1)::text').get(),
                'Fecha': row.css('td:nth-child(2)::text').get(),
                'Festivo': row.css('td:nth-child(3)::text').get(),
                'Día': row.css('td:nth-child(4)::text').get(),
            }
    
    def start_requests(self):
        urls = [
            'https://www.festivos.com.co/historico'  # Reemplaza con la URL real donde se encuentra tu tabla
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
