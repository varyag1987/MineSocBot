import scrapy


class SnebesSpider(scrapy.Spider):
    name = "snebes"

    def __init__(self, cookies=None, *args, **kwargs):
        super(SnebesSpider, self).__init__(*args, **kwargs)
        self.my_cookies = cookies

    def start_requests(self):
        urls = [
            'http://snebes.ru/tasks.php?c=2',
            'http://snebes.ru/tasks.php?c=1',
            'http://snebes.ru/tasks.php?c=4',
            'http://snebes.ru/tasks.php?c=3',
        ]
        parsers = (
            self.ParseGroup,
            self.ParseLike,
            self.ParseRepost,
            self.ParseFriend
            )
        for url, parser in zip(urls, parsers):
            yield scrapy.Request(url=url, callback=parser, cookies = self.my_cookies)

    def ParseRepost(self, response):
        loader = scrapy.ItemLoader(item=TaskRepost(), response=response)
        loader.add_xpath('repost', '//div[@class="taskurl22"]/text()', re = '\w+')
        #self.log('Saved file %s' % filename)
        print('ParseRepost')
        return loader.load_item()

    def ParseGroup(self, response):
        pass
    
    def ParseLike(self, response):
        pass

    def ParseFriend(self, response):
        pass

class TaskRepost(scrapy.Item):
    repost = scrapy.Field()

class TaskFriend(scrapy.Item):
    id = scrapy.Field()

class TaskGroup(scrapy.Item):
    id = scrapy.Field()    
        
class TaskLike(scrapy.Item):
    type_obj = scrapy.Field()
    owner_id = scrapy.Field()
    item_id = scrapy.Field()