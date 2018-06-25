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
		payload = {'name' : 'vkontakte', 'code' : 'bf4e550d9d78bfe7f2'}
		for i in range(5):
			r = self.session.get('https://ulogin.ru/auth.php', params = payload)
			#print(requests.utils.dict_from_cookiejar(r.cookies))		
			#print(r.text)
			token = re.search("token\s*=\s*'(\w*)'", r.text)
			if token is not None:
				token = token.group(1)
				break

		payload = {'token:' : token}
		r = self.session.post('http://snebes.ru', data = payload)

	def doLike(self, type_obj, owner_id, item_id):
		pass

	def addFriend(self):
		pass

	def doRepost(self):
		pass

	def joinGroup(self):
		pass