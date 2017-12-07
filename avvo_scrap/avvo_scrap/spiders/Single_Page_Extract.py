import scrapy

class AvvoTask(scrapy.Spider):

	name = "avvobot" # name of the spider
	allowed_domains = ['www.avvo.com']
	start_urls = ['https://www.avvo.com/attorneys/10924-ny-barbara-strauss-830913.html']

	def parse(self,response):
		
		name = " ".join(response.xpath('.//span[@itemprop="name"]/text()').extract())
		location = " ".join(response.xpath('.//div[@class="js-v-header-address"]/text()').extract())
		avvo_rating = " ".join(response.xpath('//span[@itemprop="ratingValue"]/text()').extract())
		#license = " ".join(response.xpath('')) 
		image = response.xpath('//img/@src').extract_first()    		
		client_rating = " ".join(response.xpath('//span[@class="sr-only"]/text()').extract_first())
		area = " ".join(response.xpath('//ol//li/a[@href]/text()').extract())
		data = {
			'Name' : name,
			'Location' : location,
			'Rating on avvo' : avvo_rating,
			'Image url' : image,
			'Client Rating' : client_rating,
			'Practice Areas' : area
			}
		yield data
