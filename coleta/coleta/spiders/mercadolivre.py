import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://www.mercadolivre.com.br/ofertas"]

    def parse(self, response):
        products = response.css("div.promotion-item__description")

        for product in products:
            
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            
            yield {
                'titulo': product.css('p.promotion-item__title::text').get(),
                'new_price_reais': prices[0] if len(prices) > 0 else None,
                'new_price_centavos': product.css('span.andes-money-amount__cents.andes-money-amount__cents--superscript-24::text').get(),
                'old_price_reais': prices[1] if len(prices) > 0 else None,
                'old_price_centavos': products.css('span.andes-money-amount__cents.andes-money-amount__cents--superscript-12::text').get() 
            }