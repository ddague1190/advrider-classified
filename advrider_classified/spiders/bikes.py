import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BikesSpider(CrawlSpider):
    name = 'bikes'
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': 1000
    }
    allowed_domains = ['advrider.com']
    start_urls = ['https://www.advrider.com/f/forums/bikes.52']

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a[@class='prefixLink']/following-sibling::a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[contains(.,'Next ') and @class='text'])[2]")),
    )

    def parse_item(self, response):
        images = response.xpath("//img[@class='bbCodeImage LbImage']/@src").extract()
        _images = response.xpath("//a[@class='LbTrigger']/@href").extract()
        for el in _images:
            if el[0:6] == 'attach':
                images.append(f"https://www.advrider.com/f/{el}")
            else:
                images.append(el)
        images = list(set(images))
        category = response.xpath("(//span[contains(@class, 'prefix')])/text()").get()
        date = response.xpath("(//span[@class='DateTime'])[1]/text()").get() or response.xpath("(//abbr[@class='DateTime'])[1]/@data-datestring").get() 
        return {
            'title': response.xpath("//div[@class='titleBar']/h1/text()").get(),
            'category': category,
            'url': response.request.url,
            'post_date': date,
            'first_post': response.xpath("(//blockquote)[1]/node()").extract(),
            'images': images
           }


        # if (category != 'Sold') and (category != 'Withdrawn From Sale'):
        #     return {
        #         'title': response.xpath("//div[@class='titleBar']/h1/text()").get(),
        #         'category': category,
        #         'url': response.request.url,
        #         'post_date': date,
        #         'first_post': response.xpath("(//blockquote)[1]/node()").extract(),
        #         'images': images
        #     }
       