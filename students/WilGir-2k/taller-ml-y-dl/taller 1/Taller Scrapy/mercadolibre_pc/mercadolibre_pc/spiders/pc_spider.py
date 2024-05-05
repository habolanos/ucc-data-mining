import scrapy

class IMDbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/']

    def parse(self, response):
        # Encuentra los contenedores de las películas en la página
        movie_containers = response.css('.ipc-poster-card')

        for container in movie_containers:
            # Extrae el título de la película
            title = container.css('.ipc-poster-card__title::text').get()

            # Extrae la cantidad de estrellas de la película
            stars = container.css('.ipc-rating-star-group--imdb::text').get()

            yield {
                'title': title.strip(),
                'stars': stars.strip() if stars else 'N/A'
            }
