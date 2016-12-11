import scrapy

from webcrawler_scrapy.items import DmozItem
from unicodedata import normalize

class DmozSpider(scrapy.Spider):
    name = "muabannhadat"
    allowed_domains = ["muabannhadat.vn"]
    
    start_urls = []
    
    for index in range(100, 101):
        url_str = "http://www.muabannhadat.vn/nha-ban-nha-pho-3535/tp-ho-chi-minh-s59?sf=dpo&so=d&p=" + str(index)
        start_urls.append(url_str)
    

    def parse(self, response):
        
        filename = response.url.split("/")[-2]
        
        array_house = response.xpath('//a[@class="title-filter-link"]/text()')
        
        array_price = response.xpath('//div[@class="col-md-3 text-right listing-price"]/text()') 
        
        array_district = response.xpath('//div[@class="col-md-3 col-xs-6 text-right"]/text()')  
        
        array_street = response.xpath('//div[@class="col-md-9 col-xs-6"]/text()')  
        
        array_date = response.xpath('//div[@class="col-lg-4 lline hidden-xs"]/text()')  
        
        print "---------------------------------------------"
        print array_street
        print len(array_street)
        print "---------------------------------------------"
        
        for index in range(len(array_house)):
            
            item = DmozItem()

            title = normalize('NFD', array_house[index].extract()).encode('ascii','ignore')
            title = title.strip(' \t\n\r')


            
            price = normalize('NFD', array_price[index].extract()).encode('ascii','ignore')
            price = price.strip(' \t\n\r')

            
            
            district  = normalize('NFD', array_district[index].extract()).encode('ascii','ignore')
            district = district.strip(' \t\n\r')

            
            street  = normalize('NFD', array_street[index].extract()).encode('ascii','ignore')
            street = street.strip(' \t\n\r')

            
            date  = normalize('NFD', array_date[index].extract()).encode('ascii','ignore')
            date = date.strip(' \t\n\r')

            item['title'] = title
            item['price'] = price
            item['district'] = district
            item['street'] = street
            item['date'] = date
            yield item
                
                 



