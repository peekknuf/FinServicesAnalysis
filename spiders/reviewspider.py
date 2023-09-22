import scrapy

class ReviewSpider(scrapy.Spider):
    name = 'Review'
    start_urls =  ['https://www.trustpilot.com/review/www.pairfinance.com']


    def parse (self, reviews):
        for reviews in reviews.css('div.styles_reviewContent__0Q2Tg'):
            yield {
                'Review:' : reviews.css('p.typography_body-l__KUYFJ.typography_appearance-default__AAY17.typography_color-black__5LYEn::text').get()
            }