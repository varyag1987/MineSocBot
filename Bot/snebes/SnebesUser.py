import requests
import re
import Bot

class SnebesUser:
	"""
	Класс для работы со http://snebes.ru
	"""
	#parser = Parser()

	def __init__(self, cookies):
		"""		
		Arguments:
		- cookies: Передаем куки из апи ВК. 
		"""
		self.is_auth = 0
		self.session = requests.Session()
		self.session.cookies.update(cookies)
		#print(self.session.cookies)

	def auth(self):
		payload = {'name' : 'vkontakte', 'code' : '8c298c37614f9961f2'}
		for i in range(5):
			r = self.session.get('https://ulogin.ru/auth.php', params = payload)
			#print(requests.utils.dict_from_cookiejar(r.cookies))		
			#print(r.text)
			token = re.search("token\s*=\s*'(\w*)'", r.text)
			if token is not None:
				token = token.group(1)
				print(token)
				break
				
		r = self.session.get('http://snebes.ru/')		

		headers = {
			'Connection': 'keep-alive',
			'Content-Length': '38',
			'Cache-Control': 'max-age=0',			
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'ru,en-US;q=0.8,en;q=0.6,cs;q=0.4',
			'Content-Type':'application/x-www-form-urlencoded',
			'Host':'snebes.ru',
			'Origin':'http://snebes.ru',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
			'Referer': 'http://snebes.ru'
		}
		payload = {'token:' : token}
		r = self.session.post('http://snebes.ru/', data = payload, headers = headers)		
		# print(r.cookies)
		# print(r.headers)
		# print(self.session.cookies)

	def doLike(self, type_obj, owner_id, item_id):
		pass

	def addFriend(self):
		pass

	def doRepost(self):
		pass

	def joinGroup(self):
		pass