import requests
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .. import snebes
from ..user import User
from ..parser.scrapyprj.spiders.snebes import SnebesSpider

#Одна биржа - один менеджер?!
#Одна биржа - много пользователей?!
class Manager():
	"""docstring for TaskManager"""
	def __init__(self, budget):
		#self.parser = parser()
		self.budget = budget
		self.CurrentBudget = 0

	def createUser(self, vk_param):
		"""
		Создать объект пользователя вк и биржи (пока только snebes)		
		Arguments:
		- param: параметры для конструктора User
		"""
		self.vkuser1 = User(vk_param)
		self.vkuser1.auth()		
		self.snebesuser1 = User(snebes.SnebesUser(self.vkuser1.handler.vk_session.http.cookies) )
		self.snebesuser1.auth()		

	def start(self):		
		settings = get_project_settings()
		process = CrawlerProcess(get_project_settings())
		print(self.snebesuser1.handler.session.cookies)
		process.crawl(SnebesSpider, cookies = requests.utils.dict_from_cookiejar(self.snebesuser1.handler.session.cookies) )
		process.start()
		# crawler = Crawler(settings)
		# spider = SnebesSpider(self.snebesuser1.handler.session.cookies)
		# crawler.crawl(spider)
		# crawler.start()
		

		