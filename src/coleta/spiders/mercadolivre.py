import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://www.mercadolivre.com.br/ofertas"]
    page_count = 1
    max_page_count = 5

    def parse(self, response):
        products = response.css("div.promotion-item__description")

        for product in products:
            
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            
            old_price_reais = None
            
            if len(prices) > 1:
                if prices[1] == "" or prices[1].isdigit() and int(prices[1]) > 0:
                    old_price_reais = prices[1]
            
            yield {
                'titulo': product.css('p.promotion-item__title::text').get(),
                'new_price_reais': prices[0] if len(prices) > 0 else None,
                'new_price_centavos': product.css('span.andes-money-amount__cents.andes-money-amount__cents--superscript-24::text').get(),
                'old_price_reais': old_price_reais,
                'old_price_centavos': product.css('span.andes-money-amount__cents.andes-money-amount__cents--superscript-12::text').get() 
            }
            
        if self.page_count <= self.max_page_count:
                
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
        
            if next_page:
                
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
        
        # next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
        # yield scrapy.Request(url=next_page, callback=self.parse)