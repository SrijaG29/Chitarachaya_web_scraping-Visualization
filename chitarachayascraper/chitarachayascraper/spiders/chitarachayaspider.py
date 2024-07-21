import scrapy

from chitarachayascraper.items import ItemDetails

class MyspiderSpider(scrapy.Spider):
    name = "chitarachayaspider"
    allowed_domains = ["chitrachaya.com"]
    start_urls = ["https://chitrachaya.com/collections"]

    def parse(self, response):
        category = ["/love","/kids","/fathers-day","/mothers-day","/gifts-for-brother","/gifts-for-sister","/sports","/home","/workplace"]
        for each in category:
            yield response.follow(str(response.url)+str(each),callback = self.category_details,cb_kwargs={'category':each})
    
    def category_details(self,response,category):
        all_items = response.css('h3.t4s-product-title a::attr(href)')
        for each_item in all_items:
            yield response.follow((str('https://chitrachaya.com')+str(each_item)),callback = self.product_details,cb_kwargs={'category': category})
        next_page = response.css("nav.t4s-pagination ul li a.t4s-pagination__item.pagination__item--prev.pagination__item-arrow ::attr(href)").get()
        if next_page is not None:
            yield response.follow((str('https://chitrachaya.com')+str(each_item)),callback = self.category_details,cb_kwargs={'category': category})

    def product_details(self,response,category):
        price1 = response.css("div.t4s-product-price ins::text").get()
        price2 = response.css(".t4s-price__sale::text").get()
        if price1 is not None:
            final_price = price1
        else:
            final_price = price2
        item_details = ItemDetails()
        item_details['category'] = category,
        item_details['name'] = response.css(".t4s-product__title::text").get(),
        item_details['no_of_reviews'] = response.css(".jdgm-prev-badge__text::text").get(),
        item_details['rating'] = response.css(".jdgm-rev-widg__summary-stars::attr(aria-label)").get(),
        item_details['delivery_time']  = response.css(".t4s-pr_delivery.t4s-ch.t4s-dn::text").get(),
        item_details['price'] = final_price,
        yield item_details
 

#response.css("nav.t4s-pagination ul li a.t4s-pagination__item.pagination__item--prev.pagination__item-arrow ::attr(href)").getall()
#name = response.css(".t4s-product__title::text").get()
#no_of_reviews = response.css(".jdgm-prev-badge__text::text").get()
#delivery_time = response.css(".t4s-pr_delivery.t4s-ch.t4s-dn::text").get()
#price1 = response.css("div.t4s-product-price ins::text").get()
#price2 = response.css(".t4s-price__sale::text").get()
